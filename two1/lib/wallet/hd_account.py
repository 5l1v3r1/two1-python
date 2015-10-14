import time
from two1.lib.bitcoin.crypto import HDKey, HDPrivateKey, HDPublicKey


class HDAccount(object):
    """ An implementation of a single HD account to be used in an HD
        wallet.

        This class handles key generation/management for both internal
        (change) and external (payout) purposes. If provided with only
        a public key, it is only useful for public key
        generation/management. If a private key is provided instead,
        private keys can be generated for signing (spending) purposes.

        Transaction signing capability is NOT provided by this class.
        This is a conscious design decision as the wallet is better
        suited to signing & spending as there may be situations
        requiring spending coins from multiple accounts in a single
        transaction.

        This relies on a data provider that derives from
        TransactionDataProvider, which provides transaction data and
        balance information for provided addresses.

    Args:
        hd_key (HDKey): Either a HDPrivateKey (enables private key
           generation) or HDPublicKey which is the root of this account.
        name (str): Name of this account
        index (int): child index of this account relative to the parent.
        data_provider (BaseProvider): A compatible data provider.
        testnet (bool): Whether or not this account will be used on testnet.
    """
    PAYOUT_CHAIN = 0
    CHANGE_CHAIN = 1
    GAP_LIMIT = 20
    DISCOVERY_INCREMENT = GAP_LIMIT
    MAX_BALANCE_UPDATE_THRESHOLD = 30  # seconds

    def __init__(self, hd_key, name, index, data_provider,
                 testnet=False, last_state=None):
        # Take in either public or private key for this account as we
        # can derive everything from it.
        if not isinstance(hd_key, HDKey):
            raise TypeError("hd_key must be a HDKey object")

        self.key = hd_key
        self.name = name
        self.index = index
        self.data_provider = data_provider
        self.testnet = testnet

        self.last_indices = [-1, -1]
        self._txn_cache = {}
        self._address_cache = {self.CHANGE_CHAIN: {}, self.PAYOUT_CHAIN: {}}
        self._last_balance_update = 0

        if last_state is not None and isinstance(last_state, dict):
            if "last_payout_index" in last_state:
                self.last_indices[self.PAYOUT_CHAIN] = last_state["last_payout_index"]
            if "last_change_index" in last_state:
                self.last_indices[self.CHANGE_CHAIN] = last_state["last_change_index"]
            if "addresses" in last_state:
                self._address_cache = last_state["addresses"]
            if "transactions" in last_state:
                self._txn_cache = last_state["transactions"]

        # Check to see that the address cache has up to last_indices
        for change in [self.PAYOUT_CHAIN, self.CHANGE_CHAIN]:
            k = sorted(list(self._address_cache[change].keys()))
            for i in range(self.last_indices[change] + 1):
                if i not in k or k[i] != i:
                    self.last_indices[change] = -1
                    break

        self._chain_priv_keys = [None, None]
        self._chain_pub_keys = [None, None]

        for change in [0, 1]:
            if isinstance(self.key, HDPrivateKey):
                self._chain_priv_keys[change] = HDPrivateKey.from_parent(self.key, change)
                self._chain_pub_keys[change] = self._chain_priv_keys[change].public_key
            else:
                self._chain_pub_keys[change] = HDPublicKey.from_parent(self.key, change)

        self._discover_used_addresses()
        self._update_balance()

    def _discover_used_addresses(self, max_index=0, check_all=False):
        for change in [0, 1]:
            found_last = False
            current_last = self.last_indices[change]
            addr_range = 0 if check_all else current_last + 1
            while not found_last:
                # Try a 2 * GAP_LIMIT at a go
                end = addr_range + self.DISCOVERY_INCREMENT
                addresses = {}
                addresses_to_retrieve = []

                for i in range(addr_range, end):
                    addresses[i] = self.get_address(change, i)

                    # Check any addresses we may have in the cache
                    if addresses[i] not in self._txn_cache or \
                       not self._txn_cache[addresses[i]]:
                        addresses_to_retrieve.append(addresses[i])

                txns = self.data_provider.get_transactions(addresses_to_retrieve, 10000)

                for i in sorted(addresses.keys()):
                    addr = addresses[i]
                    if i not in self._address_cache[change]:
                        self._address_cache[change][i] = addr
                    else:
                        assert self._address_cache[change][i] == addr

                    if addr not in self._txn_cache or not self._txn_cache[addr] or \
                       addr not in txns or not bool(txns[addr]):
                        if i - current_last >= self.GAP_LIMIT:
                            found_last = True
                            break

                    if addr in self._txn_cache and self._txn_cache[addr]:
                        current_last = i
                    elif bool(txns[addr]):
                        # For now we keep only txn hashes
                        # around. Revisit later.
                        seen = set()
                        for t in txns[addr]:
                            txid = str(t.hash)
                            seen.add(txid)
                        self._txn_cache[addr] = list(seen)

                        current_last = i

                addr_range += self.DISCOVERY_INCREMENT

            self.last_indices[change] = current_last

    def _update_balance(self):
        address_balances = self.data_provider.get_balance(self.all_used_addresses)

        balance = {'confirmed': 0, 'total': 0}
        for k, v in address_balances.items():
            balance['confirmed'] += v['confirmed']
            balance['total'] += v['total']

        self._balance_cache = balance
        self._last_balance_update = time.time()
        
    def has_txns(self):
        """ Returns whether or not there are any discovered transactions
            associated with any address in the account.

        Returns:
            bool: True if there are discovered transactions, False otherwise.
        """
        return bool(self._txn_cache)

    def find_addresses(self, addresses):
        """ Searches both the change and payout chains up to self.GAP_LIMIT
            addresses beyond the last known index for the chain.

        Args:
            addresses (list(str)): List of Base58Check encoded addresses

        Returns:
            dict: Dictionary keyed by address where the value is a tuple
               containing the chain (0 or 1) and child index in the chain.
               Only found addresses are included in the dict.
        """
        found = {}
        for change in [0, 1]:
            for i in range(self.last_indices[change] + self.GAP_LIMIT + 1):
                addr = self.get_address(change, i)

                if addr in addresses:
                    found[addr] = (self.index, change, i)

        return found

    def get_public_key(self, change, n=-1):
        """ Returns a public key in the chain

        Args:
            change (bool): If True, returns an address for change purposes,
               otherwise returns an address for payment.
            n (int): index of address in chain. If n == -1, a new key
               is created with index = self.last_[change|payout]_index + 1

        Returns:
            HDPublicKey: a public key in this account's chain.
        """
        # We only use public key derivation per BIP44
        c = int(change)
        k = self._chain_pub_keys[c]
        if n < 0:
            self.last_indices[c] += 1
            i = self.last_indices[c]
            pub_key = HDPublicKey.from_parent(k, i)
            addr = pub_key.address(True, self.testnet)
            if i not in self._address_cache[c]:
                self._address_cache[c][i] = addr
            else:
                # Make sure it's the same
                assert self._address_cache[c][i] == addr
        else:
            pub_key = HDPublicKey.from_parent(k, n)

        return pub_key

    def get_private_key(self, change, n):
        """ Returns a private key in the chain for use in signing messages
            or transactions.

        Args:
            change (bool): If True, returns an address for change purposes,
               otherwise returns an address for payment.
            n (int): index of address in chain.

        Returns:
            HDPrivateKey: a private key in this account's chain.
        """
        # We only use public key derivation per BIP44
        k = self._chain_priv_keys[change]
        if k is None:
            raise ValueError("No private key provided for account.")
        return HDPrivateKey.from_parent(k, n)

    def get_address(self, change, n=-1):
        """ Returns a public address

        Args:
            change (bool): If True, returns an address for change purposes,
               otherwise returns an address for payment.
            n (int): index of address in chain. If n == -1, a new key
               is created with index = self.last_[change|payout]_index + 1

        Returns:
            str: A bitcoin address
        """
        # If this is an address we've already generated, don't regenerate.
        c = int(change)
        if n in self._address_cache[c]:
            return self._address_cache[c][n]

        # Always do compressed keys
        return self.get_public_key(change, n).address(True, self.testnet)

    def _new_key_or_address(self, change, key=False):
        c = int(change)
        last_index = self.last_indices[c]

        # Check to see if the current address has any txns
        # associated with it before giving out a new one.
        ret = None
        need_new = False
        if last_index >= 0:
            current_addr = self._address_cache[c][last_index]
            txns = self.data_provider.get_transactions([current_addr])
            need_new = current_addr in txns and txns[current_addr]
        else:
            need_new = True

        if need_new:
            ret = self.get_public_key(change) if key else self.get_address(change)
        else:
            ret = self.get_public_key(change, last_index) if key else current_addr

        return ret

    def get_next_address(self, change):
        """ Returns the next public address in the specified chain.

            A new address is only returned if there are transactions found
            for the current address.

        Args:
            change (bool): If True, returns an address for change purposes,
               otherwise returns an address for payment.

        Returns:
            str: A bitcoin address
        """
        return self._new_key_or_address(change)

    def get_next_public_key(self, change):
        """ Returns the next public key in the specified chain.

            A new key is only returned if there are transactions found
            for the current key.

        Args:
            change (bool): If True, returns a PublicKey for change purposes,
               otherwise returns a PublicKey for payment.

        Returns:
            PublicKey: A public key
        """
        return self._new_key_or_address(change, True)

    def get_utxos(self):
        """ Gets all unspent transactions associated with all addresses
            up to and including the last known indices for both change
            and payout chains.
        """
        return self.data_provider.get_utxos(self.all_used_addresses)

    @property
    def address_cache(self):
        """ Returns the address cache
        """
        return self._address_cache

    @property
    def transaction_cache(self):
        """ Returns the transaction cache
        """
        return self._txn_cache

    def to_dict(self):
        """ Returns a JSON-serializable dict to save account data

        Returns:
            dict: Dict that can be serialized into a JSON string
        """
        if isinstance(self.key, HDPublicKey):
            pub_key = self.key
        else:
            pub_key = self.key.public_key
        return {"public_key": pub_key.to_b58check(self.testnet),
                "last_payout_index": self.last_indices[self.PAYOUT_CHAIN],
                "last_change_index": self.last_indices[self.CHANGE_CHAIN]}

    @property
    def balance(self):
        """ Returns balances, both confirmed and total, for this
            account.

        Returns:
            dict: 'confirmed' and 'total' keys with balance values in
                satoshis for each. The total balance includes
                unconfirmed transactions.
        """
        if time.time() - self._last_balance_update > self.MAX_BALANCE_UPDATE_THRESHOLD:
            self._update_balance()
        return self._balance_cache

    @property
    def all_used_addresses(self):
        """ List of all used addresses

        Returns:
            list(str): list of all used addresses (Base58Check encoded)
        """
        all_addresses = []
        for change in [self.PAYOUT_CHAIN, self.CHANGE_CHAIN]:
            last = self.last_indices[change]
            all_addresses += [v for k, v in self._address_cache[change].items() if k <= last]

        return all_addresses

    @property
    def current_change_address(self):
        """ Returns the current change address

        Returns:
            str: Base58Check-encoded string containing the current
               change address.
        """
        return self.get_address(True, self.last_indices[self.CHANGE_CHAIN])

    @property
    def current_payout_address(self):
        """ Returns the current payout address

        Returns:
            str: Base58Check-encoded string containing the current
               payout address.
        """
        return self.get_address(False, self.last_indices[self.PAYOUT_CHAIN])