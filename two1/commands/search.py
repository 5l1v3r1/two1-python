import click
from two1.config import pass_config

@click.command()
@pass_config
def search(config, query="translation", reverse=False):
    "Search the Many Machine Market (MMM)"
    print("Searching the MMM for %s" % query)
    return query