# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: laminar.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='laminar.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rlaminar.proto\"\xa7\x03\n\x14LaminarClientMessage\x12J\n\x15\x62itshare_auth_request\x18\x01 \x01(\x0b\x32).LaminarClientMessage.BitshareAuthRequestH\x00\x12\x42\n\x0esubmit_request\x18\x02 \x01(\x0b\x32(.LaminarClientMessage.SubmitShareRequestH\x00\x1a\x83\x01\n\x13\x42itshareAuthRequest\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x10\n\x08username\x18\x02 \x01(\x0c\x12\x0b\n\x03mac\x18\x03 \x01(\x0c\x12\x14\n\x0cwallet_index\x18\x04 \x01(\r\x12\x11\n\tnumerator\x18\x05 \x01(\r\x12\x13\n\x0b\x64\x65nominator\x18\x06 \x01(\r\x1ag\n\x12SubmitShareRequest\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x0e\n\x06job_id\x18\x02 \x01(\r\x12\x0f\n\x07\x65nonce2\x18\x03 \x01(\x0c\x12\r\n\x05otime\x18\x04 \x01(\r\x12\r\n\x05nonce\x18\x05 \x01(\rB\x10\n\x0e\x63lientmessages\"\xef\x07\n\x14LaminarServerMessage\x12\x35\n\nauth_reply\x18\x01 \x01(\x0b\x32\x1f.LaminarServerMessage.AuthReplyH\x00\x12>\n\x0csubmit_reply\x18\x02 \x01(\x0b\x32&.LaminarServerMessage.SubmitShareReplyH\x00\x12\x43\n\x11work_notification\x18\x03 \x01(\x0b\x32&.LaminarServerMessage.WorkNotificationH\x00\x1a\x8d\x03\n\tAuthReply\x12\x46\n\x0e\x61uth_reply_yes\x18\x01 \x01(\x0b\x32,.LaminarServerMessage.AuthReply.AuthReplyYesH\x00\x12\x44\n\rauth_reply_no\x18\x02 \x01(\x0b\x32+.LaminarServerMessage.AuthReply.AuthReplyNoH\x00\x12Q\n\x14\x61uth_reply_pool_down\x18\x03 \x01(\x0b\x32\x31.LaminarServerMessage.AuthReply.AuthReplyPoolDownH\x00\x1a\x35\n\x0c\x41uthReplyYes\x12\x0f\n\x07\x65nonce1\x18\x01 \x01(\x0c\x12\x14\n\x0c\x65nonce2_size\x18\x02 \x01(\r\x1a\x1c\n\x0b\x41uthReplyNo\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x1a;\n\x11\x41uthReplyPoolDown\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x15\n\rretry_seconds\x18\x02 \x01(\rB\r\n\x0b\x61uthreplies\x1a\xaf\x01\n\x10SubmitShareReply\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12J\n\rsubmit_status\x18\x02 \x01(\x0e\x32\x33.LaminarServerMessage.SubmitShareReply.SubmitStatus\";\n\x0cSubmitStatus\x12\x07\n\x03\x62\x61\x64\x10\x00\x12\x08\n\x04good\x10\x01\x12\t\n\x05stale\x10\x02\x12\r\n\tduplicate\x10\x03\x1a\xc6\x01\n\x10WorkNotification\x12\x0e\n\x06job_id\x18\x01 \x01(\r\x12\x15\n\rblock_version\x18\x02 \x01(\r\x12\x0c\n\x04prev\x18\x03 \x01(\x0c\x12\x0e\n\x06height\x18\x04 \x01(\r\x12\x0c\n\x04\x62its\x18\x05 \x01(\r\x12\r\n\x05itime\x18\x06 \x01(\r\x12\x10\n\x08iscript0\x18\x07 \x01(\x0c\x12\x10\n\x08iscript1\x18\x08 \x01(\x0c\x12\x0f\n\x07outputs\x18\t \x03(\x0c\x12\x0c\n\x04\x65\x64ge\x18\n \x03(\x0c\x12\r\n\x05\x63lear\x18\x0b \x01(\x08\x42\x10\n\x0eservermessagesb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY_SUBMITSTATUS = _descriptor.EnumDescriptor(
  name='SubmitStatus',
  full_name='LaminarServerMessage.SubmitShareReply.SubmitStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='bad', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='good', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stale', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='duplicate', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1173,
  serialized_end=1232,
)
_sym_db.RegisterEnumDescriptor(_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY_SUBMITSTATUS)


_LAMINARCLIENTMESSAGE_BITSHAREAUTHREQUEST = _descriptor.Descriptor(
  name='BitshareAuthRequest',
  full_name='LaminarClientMessage.BitshareAuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='LaminarClientMessage.BitshareAuthRequest.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='LaminarClientMessage.BitshareAuthRequest.username', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac', full_name='LaminarClientMessage.BitshareAuthRequest.mac', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wallet_index', full_name='LaminarClientMessage.BitshareAuthRequest.wallet_index', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numerator', full_name='LaminarClientMessage.BitshareAuthRequest.numerator', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='denominator', full_name='LaminarClientMessage.BitshareAuthRequest.denominator', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=318,
)

_LAMINARCLIENTMESSAGE_SUBMITSHAREREQUEST = _descriptor.Descriptor(
  name='SubmitShareRequest',
  full_name='LaminarClientMessage.SubmitShareRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='LaminarClientMessage.SubmitShareRequest.message_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='LaminarClientMessage.SubmitShareRequest.job_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enonce2', full_name='LaminarClientMessage.SubmitShareRequest.enonce2', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otime', full_name='LaminarClientMessage.SubmitShareRequest.otime', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='LaminarClientMessage.SubmitShareRequest.nonce', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=423,
)

_LAMINARCLIENTMESSAGE = _descriptor.Descriptor(
  name='LaminarClientMessage',
  full_name='LaminarClientMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bitshare_auth_request', full_name='LaminarClientMessage.bitshare_auth_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submit_request', full_name='LaminarClientMessage.submit_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LAMINARCLIENTMESSAGE_BITSHAREAUTHREQUEST, _LAMINARCLIENTMESSAGE_SUBMITSHAREREQUEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='clientmessages', full_name='LaminarClientMessage.clientmessages',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=18,
  serialized_end=441,
)


_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYYES = _descriptor.Descriptor(
  name='AuthReplyYes',
  full_name='LaminarServerMessage.AuthReply.AuthReplyYes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enonce1', full_name='LaminarServerMessage.AuthReply.AuthReplyYes.enonce1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enonce2_size', full_name='LaminarServerMessage.AuthReply.AuthReplyYes.enonce2_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=948,
)

_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYNO = _descriptor.Descriptor(
  name='AuthReplyNo',
  full_name='LaminarServerMessage.AuthReply.AuthReplyNo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='LaminarServerMessage.AuthReply.AuthReplyNo.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=978,
)

_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYPOOLDOWN = _descriptor.Descriptor(
  name='AuthReplyPoolDown',
  full_name='LaminarServerMessage.AuthReply.AuthReplyPoolDown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='LaminarServerMessage.AuthReply.AuthReplyPoolDown.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retry_seconds', full_name='LaminarServerMessage.AuthReply.AuthReplyPoolDown.retry_seconds', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=980,
  serialized_end=1039,
)

_LAMINARSERVERMESSAGE_AUTHREPLY = _descriptor.Descriptor(
  name='AuthReply',
  full_name='LaminarServerMessage.AuthReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_reply_yes', full_name='LaminarServerMessage.AuthReply.auth_reply_yes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_reply_no', full_name='LaminarServerMessage.AuthReply.auth_reply_no', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_reply_pool_down', full_name='LaminarServerMessage.AuthReply.auth_reply_pool_down', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYYES, _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYNO, _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYPOOLDOWN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='authreplies', full_name='LaminarServerMessage.AuthReply.authreplies',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=657,
  serialized_end=1054,
)

_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY = _descriptor.Descriptor(
  name='SubmitShareReply',
  full_name='LaminarServerMessage.SubmitShareReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='LaminarServerMessage.SubmitShareReply.message_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submit_status', full_name='LaminarServerMessage.SubmitShareReply.submit_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY_SUBMITSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1057,
  serialized_end=1232,
)

_LAMINARSERVERMESSAGE_WORKNOTIFICATION = _descriptor.Descriptor(
  name='WorkNotification',
  full_name='LaminarServerMessage.WorkNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='LaminarServerMessage.WorkNotification.job_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block_version', full_name='LaminarServerMessage.WorkNotification.block_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prev', full_name='LaminarServerMessage.WorkNotification.prev', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='LaminarServerMessage.WorkNotification.height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bits', full_name='LaminarServerMessage.WorkNotification.bits', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itime', full_name='LaminarServerMessage.WorkNotification.itime', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iscript0', full_name='LaminarServerMessage.WorkNotification.iscript0', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iscript1', full_name='LaminarServerMessage.WorkNotification.iscript1', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='LaminarServerMessage.WorkNotification.outputs', index=8,
      number=9, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edge', full_name='LaminarServerMessage.WorkNotification.edge', index=9,
      number=10, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clear', full_name='LaminarServerMessage.WorkNotification.clear', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1235,
  serialized_end=1433,
)

_LAMINARSERVERMESSAGE = _descriptor.Descriptor(
  name='LaminarServerMessage',
  full_name='LaminarServerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auth_reply', full_name='LaminarServerMessage.auth_reply', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='submit_reply', full_name='LaminarServerMessage.submit_reply', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_notification', full_name='LaminarServerMessage.work_notification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LAMINARSERVERMESSAGE_AUTHREPLY, _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY, _LAMINARSERVERMESSAGE_WORKNOTIFICATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='servermessages', full_name='LaminarServerMessage.servermessages',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=444,
  serialized_end=1451,
)

_LAMINARCLIENTMESSAGE_BITSHAREAUTHREQUEST.containing_type = _LAMINARCLIENTMESSAGE
_LAMINARCLIENTMESSAGE_SUBMITSHAREREQUEST.containing_type = _LAMINARCLIENTMESSAGE
_LAMINARCLIENTMESSAGE.fields_by_name['bitshare_auth_request'].message_type = _LAMINARCLIENTMESSAGE_BITSHAREAUTHREQUEST
_LAMINARCLIENTMESSAGE.fields_by_name['submit_request'].message_type = _LAMINARCLIENTMESSAGE_SUBMITSHAREREQUEST
_LAMINARCLIENTMESSAGE.oneofs_by_name['clientmessages'].fields.append(
  _LAMINARCLIENTMESSAGE.fields_by_name['bitshare_auth_request'])
_LAMINARCLIENTMESSAGE.fields_by_name['bitshare_auth_request'].containing_oneof = _LAMINARCLIENTMESSAGE.oneofs_by_name['clientmessages']
_LAMINARCLIENTMESSAGE.oneofs_by_name['clientmessages'].fields.append(
  _LAMINARCLIENTMESSAGE.fields_by_name['submit_request'])
_LAMINARCLIENTMESSAGE.fields_by_name['submit_request'].containing_oneof = _LAMINARCLIENTMESSAGE.oneofs_by_name['clientmessages']
_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYYES.containing_type = _LAMINARSERVERMESSAGE_AUTHREPLY
_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYNO.containing_type = _LAMINARSERVERMESSAGE_AUTHREPLY
_LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYPOOLDOWN.containing_type = _LAMINARSERVERMESSAGE_AUTHREPLY
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_yes'].message_type = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYYES
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_no'].message_type = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYNO
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_pool_down'].message_type = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYPOOLDOWN
_LAMINARSERVERMESSAGE_AUTHREPLY.containing_type = _LAMINARSERVERMESSAGE
_LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies'].fields.append(
  _LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_yes'])
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_yes'].containing_oneof = _LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies']
_LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies'].fields.append(
  _LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_no'])
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_no'].containing_oneof = _LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies']
_LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies'].fields.append(
  _LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_pool_down'])
_LAMINARSERVERMESSAGE_AUTHREPLY.fields_by_name['auth_reply_pool_down'].containing_oneof = _LAMINARSERVERMESSAGE_AUTHREPLY.oneofs_by_name['authreplies']
_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY.fields_by_name['submit_status'].enum_type = _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY_SUBMITSTATUS
_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY.containing_type = _LAMINARSERVERMESSAGE
_LAMINARSERVERMESSAGE_SUBMITSHAREREPLY_SUBMITSTATUS.containing_type = _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY
_LAMINARSERVERMESSAGE_WORKNOTIFICATION.containing_type = _LAMINARSERVERMESSAGE
_LAMINARSERVERMESSAGE.fields_by_name['auth_reply'].message_type = _LAMINARSERVERMESSAGE_AUTHREPLY
_LAMINARSERVERMESSAGE.fields_by_name['submit_reply'].message_type = _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY
_LAMINARSERVERMESSAGE.fields_by_name['work_notification'].message_type = _LAMINARSERVERMESSAGE_WORKNOTIFICATION
_LAMINARSERVERMESSAGE.oneofs_by_name['servermessages'].fields.append(
  _LAMINARSERVERMESSAGE.fields_by_name['auth_reply'])
_LAMINARSERVERMESSAGE.fields_by_name['auth_reply'].containing_oneof = _LAMINARSERVERMESSAGE.oneofs_by_name['servermessages']
_LAMINARSERVERMESSAGE.oneofs_by_name['servermessages'].fields.append(
  _LAMINARSERVERMESSAGE.fields_by_name['submit_reply'])
_LAMINARSERVERMESSAGE.fields_by_name['submit_reply'].containing_oneof = _LAMINARSERVERMESSAGE.oneofs_by_name['servermessages']
_LAMINARSERVERMESSAGE.oneofs_by_name['servermessages'].fields.append(
  _LAMINARSERVERMESSAGE.fields_by_name['work_notification'])
_LAMINARSERVERMESSAGE.fields_by_name['work_notification'].containing_oneof = _LAMINARSERVERMESSAGE.oneofs_by_name['servermessages']
DESCRIPTOR.message_types_by_name['LaminarClientMessage'] = _LAMINARCLIENTMESSAGE
DESCRIPTOR.message_types_by_name['LaminarServerMessage'] = _LAMINARSERVERMESSAGE

LaminarClientMessage = _reflection.GeneratedProtocolMessageType('LaminarClientMessage', (_message.Message,), dict(

  BitshareAuthRequest = _reflection.GeneratedProtocolMessageType('BitshareAuthRequest', (_message.Message,), dict(
    DESCRIPTOR = _LAMINARCLIENTMESSAGE_BITSHAREAUTHREQUEST,
    __module__ = 'laminar_pb2'
    # @@protoc_insertion_point(class_scope:LaminarClientMessage.BitshareAuthRequest)
    ))
  ,

  SubmitShareRequest = _reflection.GeneratedProtocolMessageType('SubmitShareRequest', (_message.Message,), dict(
    DESCRIPTOR = _LAMINARCLIENTMESSAGE_SUBMITSHAREREQUEST,
    __module__ = 'laminar_pb2'
    # @@protoc_insertion_point(class_scope:LaminarClientMessage.SubmitShareRequest)
    ))
  ,
  DESCRIPTOR = _LAMINARCLIENTMESSAGE,
  __module__ = 'laminar_pb2'
  # @@protoc_insertion_point(class_scope:LaminarClientMessage)
  ))
_sym_db.RegisterMessage(LaminarClientMessage)
_sym_db.RegisterMessage(LaminarClientMessage.BitshareAuthRequest)
_sym_db.RegisterMessage(LaminarClientMessage.SubmitShareRequest)

LaminarServerMessage = _reflection.GeneratedProtocolMessageType('LaminarServerMessage', (_message.Message,), dict(

  AuthReply = _reflection.GeneratedProtocolMessageType('AuthReply', (_message.Message,), dict(

    AuthReplyYes = _reflection.GeneratedProtocolMessageType('AuthReplyYes', (_message.Message,), dict(
      DESCRIPTOR = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYYES,
      __module__ = 'laminar_pb2'
      # @@protoc_insertion_point(class_scope:LaminarServerMessage.AuthReply.AuthReplyYes)
      ))
    ,

    AuthReplyNo = _reflection.GeneratedProtocolMessageType('AuthReplyNo', (_message.Message,), dict(
      DESCRIPTOR = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYNO,
      __module__ = 'laminar_pb2'
      # @@protoc_insertion_point(class_scope:LaminarServerMessage.AuthReply.AuthReplyNo)
      ))
    ,

    AuthReplyPoolDown = _reflection.GeneratedProtocolMessageType('AuthReplyPoolDown', (_message.Message,), dict(
      DESCRIPTOR = _LAMINARSERVERMESSAGE_AUTHREPLY_AUTHREPLYPOOLDOWN,
      __module__ = 'laminar_pb2'
      # @@protoc_insertion_point(class_scope:LaminarServerMessage.AuthReply.AuthReplyPoolDown)
      ))
    ,
    DESCRIPTOR = _LAMINARSERVERMESSAGE_AUTHREPLY,
    __module__ = 'laminar_pb2'
    # @@protoc_insertion_point(class_scope:LaminarServerMessage.AuthReply)
    ))
  ,

  SubmitShareReply = _reflection.GeneratedProtocolMessageType('SubmitShareReply', (_message.Message,), dict(
    DESCRIPTOR = _LAMINARSERVERMESSAGE_SUBMITSHAREREPLY,
    __module__ = 'laminar_pb2'
    # @@protoc_insertion_point(class_scope:LaminarServerMessage.SubmitShareReply)
    ))
  ,

  WorkNotification = _reflection.GeneratedProtocolMessageType('WorkNotification', (_message.Message,), dict(
    DESCRIPTOR = _LAMINARSERVERMESSAGE_WORKNOTIFICATION,
    __module__ = 'laminar_pb2'
    # @@protoc_insertion_point(class_scope:LaminarServerMessage.WorkNotification)
    ))
  ,
  DESCRIPTOR = _LAMINARSERVERMESSAGE,
  __module__ = 'laminar_pb2'
  # @@protoc_insertion_point(class_scope:LaminarServerMessage)
  ))
_sym_db.RegisterMessage(LaminarServerMessage)
_sym_db.RegisterMessage(LaminarServerMessage.AuthReply)
_sym_db.RegisterMessage(LaminarServerMessage.AuthReply.AuthReplyYes)
_sym_db.RegisterMessage(LaminarServerMessage.AuthReply.AuthReplyNo)
_sym_db.RegisterMessage(LaminarServerMessage.AuthReply.AuthReplyPoolDown)
_sym_db.RegisterMessage(LaminarServerMessage.SubmitShareReply)
_sym_db.RegisterMessage(LaminarServerMessage.WorkNotification)


# @@protoc_insertion_point(module_scope)