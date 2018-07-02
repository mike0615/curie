# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: charon_agent_interface.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import curie_extensions_pb2 as curie__extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='charon_agent_interface.proto',
  package='nutanix.curie',
  syntax='proto2',
  serialized_pb=_b('\n\x1c\x63haron_agent_interface.proto\x12\rnutanix.curie\x1a\x16\x63urie_extensions.proto\"\xd4\x01\n\tCmdStatus\x12,\n\x05state\x18\x01 \x02(\x0e\x32\x1d.nutanix.curie.CmdStatus.Type\x12\x0b\n\x03pid\x18\x02 \x01(\x05\x12\x13\n\x0b\x65xit_status\x18\x03 \x01(\x05\x12\x13\n\x0bstdout_path\x18\x04 \x01(\t\x12\x13\n\x0bstderr_path\x18\x05 \x01(\t\"M\n\x04Type\x12\x0c\n\x08kRunning\x10\x00\x12\x0e\n\nkSucceeded\x10\x01\x12\x0b\n\x07kFailed\x10\x02\x12\x0c\n\x08kStopped\x10\x03\x12\x0c\n\x08kUnknown\x10\x04\"C\n\rCmdExecuteArg\x12\x15\n\x04user\x18\x01 \x01(\t:\x07nutanix\x12\x0e\n\x06\x63md_id\x18\x02 \x02(\t\x12\x0b\n\x03\x63md\x18\x03 \x02(\t\"\x0f\n\rCmdExecuteRet\"=\n\x0c\x43mdStatusArg\x12\x0e\n\x06\x63md_id\x18\x01 \x02(\t\x12\x1d\n\x0einclude_output\x18\x02 \x01(\x08:\x05\x66\x61lse\"\\\n\x0c\x43mdStatusRet\x12,\n\ncmd_status\x18\x01 \x02(\x0b\x32\x18.nutanix.curie.CmdStatus\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12\x0e\n\x06stderr\x18\x03 \x01(\t\"\x1c\n\nCmdStopArg\x12\x0e\n\x06\x63md_id\x18\x01 \x02(\t\"\x0c\n\nCmdStopRet\"\x1e\n\x0c\x43mdRemoveArg\x12\x0e\n\x06\x63md_id\x18\x01 \x02(\t\"\x0e\n\x0c\x43mdRemoveRet\"\x0c\n\nCmdListArg\"\xa5\x01\n\nCmdListRet\x12>\n\x10\x63md_summary_list\x18\x01 \x03(\x0b\x32$.nutanix.curie.CmdListRet.CmdSummary\x1aW\n\nCmdSummary\x12\x0e\n\x06\x63md_id\x18\x01 \x02(\t\x12\x0b\n\x03\x63md\x18\x02 \x02(\t\x12,\n\x05state\x18\x03 \x02(\x0e\x32\x1d.nutanix.curie.CmdStatus.Type\"=\n\nFileGetArg\x12\x0c\n\x04path\x18\x01 \x02(\t\x12\x11\n\x06offset\x18\x02 \x01(\x03:\x01\x30\x12\x0e\n\x06length\x18\x03 \x01(\x03\"\x1a\n\nFileGetRet\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x32\xb8\x03\n\x10\x43urieAgentRpcSvc\x12H\n\nCmdExecute\x12\x1c.nutanix.curie.CmdExecuteArg\x1a\x1c.nutanix.curie.CmdExecuteRet\x12\x45\n\tCmdStatus\x12\x1b.nutanix.curie.CmdStatusArg\x1a\x1b.nutanix.curie.CmdStatusRet\x12?\n\x07\x43mdStop\x12\x19.nutanix.curie.CmdStopArg\x1a\x19.nutanix.curie.CmdStopRet\x12\x45\n\tCmdRemove\x12\x1b.nutanix.curie.CmdRemoveArg\x1a\x1b.nutanix.curie.CmdRemoveRet\x12?\n\x07\x43mdList\x12\x19.nutanix.curie.CmdListArg\x1a\x19.nutanix.curie.CmdListRet\x12?\n\x07\x46ileGet\x12\x19.nutanix.curie.FileGetArg\x1a\x19.nutanix.curie.FileGetRet\x1a\t\xc0\xf3\x18\xe8\x07\xc8\xf3\x18\x14\x42\x03\x90\x01\x01')
  ,
  dependencies=[curie__extensions__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CMDSTATUS_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='nutanix.curie.CmdStatus.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kRunning', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSucceeded', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kFailed', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kStopped', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kUnknown', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=207,
  serialized_end=284,
)
_sym_db.RegisterEnumDescriptor(_CMDSTATUS_TYPE)


_CMDSTATUS = _descriptor.Descriptor(
  name='CmdStatus',
  full_name='nutanix.curie.CmdStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='nutanix.curie.CmdStatus.state', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pid', full_name='nutanix.curie.CmdStatus.pid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exit_status', full_name='nutanix.curie.CmdStatus.exit_status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stdout_path', full_name='nutanix.curie.CmdStatus.stdout_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stderr_path', full_name='nutanix.curie.CmdStatus.stderr_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CMDSTATUS_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=284,
)


_CMDEXECUTEARG = _descriptor.Descriptor(
  name='CmdExecuteArg',
  full_name='nutanix.curie.CmdExecuteArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='nutanix.curie.CmdExecuteArg.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("nutanix").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmd_id', full_name='nutanix.curie.CmdExecuteArg.cmd_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='nutanix.curie.CmdExecuteArg.cmd', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=353,
)


_CMDEXECUTERET = _descriptor.Descriptor(
  name='CmdExecuteRet',
  full_name='nutanix.curie.CmdExecuteRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=355,
  serialized_end=370,
)


_CMDSTATUSARG = _descriptor.Descriptor(
  name='CmdStatusArg',
  full_name='nutanix.curie.CmdStatusArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_id', full_name='nutanix.curie.CmdStatusArg.cmd_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_output', full_name='nutanix.curie.CmdStatusArg.include_output', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=433,
)


_CMDSTATUSRET = _descriptor.Descriptor(
  name='CmdStatusRet',
  full_name='nutanix.curie.CmdStatusRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_status', full_name='nutanix.curie.CmdStatusRet.cmd_status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stdout', full_name='nutanix.curie.CmdStatusRet.stdout', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='nutanix.curie.CmdStatusRet.stderr', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=527,
)


_CMDSTOPARG = _descriptor.Descriptor(
  name='CmdStopArg',
  full_name='nutanix.curie.CmdStopArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_id', full_name='nutanix.curie.CmdStopArg.cmd_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=557,
)


_CMDSTOPRET = _descriptor.Descriptor(
  name='CmdStopRet',
  full_name='nutanix.curie.CmdStopRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=571,
)


_CMDREMOVEARG = _descriptor.Descriptor(
  name='CmdRemoveArg',
  full_name='nutanix.curie.CmdRemoveArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_id', full_name='nutanix.curie.CmdRemoveArg.cmd_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=573,
  serialized_end=603,
)


_CMDREMOVERET = _descriptor.Descriptor(
  name='CmdRemoveRet',
  full_name='nutanix.curie.CmdRemoveRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=619,
)


_CMDLISTARG = _descriptor.Descriptor(
  name='CmdListArg',
  full_name='nutanix.curie.CmdListArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=621,
  serialized_end=633,
)


_CMDLISTRET_CMDSUMMARY = _descriptor.Descriptor(
  name='CmdSummary',
  full_name='nutanix.curie.CmdListRet.CmdSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_id', full_name='nutanix.curie.CmdListRet.CmdSummary.cmd_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='nutanix.curie.CmdListRet.CmdSummary.cmd', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='nutanix.curie.CmdListRet.CmdSummary.state', index=2,
      number=3, type=14, cpp_type=8, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=714,
  serialized_end=801,
)

_CMDLISTRET = _descriptor.Descriptor(
  name='CmdListRet',
  full_name='nutanix.curie.CmdListRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmd_summary_list', full_name='nutanix.curie.CmdListRet.cmd_summary_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CMDLISTRET_CMDSUMMARY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=636,
  serialized_end=801,
)


_FILEGETARG = _descriptor.Descriptor(
  name='FileGetArg',
  full_name='nutanix.curie.FileGetArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='nutanix.curie.FileGetArg.path', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='offset', full_name='nutanix.curie.FileGetArg.offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='nutanix.curie.FileGetArg.length', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=803,
  serialized_end=864,
)


_FILEGETRET = _descriptor.Descriptor(
  name='FileGetRet',
  full_name='nutanix.curie.FileGetRet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='nutanix.curie.FileGetRet.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=892,
)

_CMDSTATUS.fields_by_name['state'].enum_type = _CMDSTATUS_TYPE
_CMDSTATUS_TYPE.containing_type = _CMDSTATUS
_CMDSTATUSRET.fields_by_name['cmd_status'].message_type = _CMDSTATUS
_CMDLISTRET_CMDSUMMARY.fields_by_name['state'].enum_type = _CMDSTATUS_TYPE
_CMDLISTRET_CMDSUMMARY.containing_type = _CMDLISTRET
_CMDLISTRET.fields_by_name['cmd_summary_list'].message_type = _CMDLISTRET_CMDSUMMARY
DESCRIPTOR.message_types_by_name['CmdStatus'] = _CMDSTATUS
DESCRIPTOR.message_types_by_name['CmdExecuteArg'] = _CMDEXECUTEARG
DESCRIPTOR.message_types_by_name['CmdExecuteRet'] = _CMDEXECUTERET
DESCRIPTOR.message_types_by_name['CmdStatusArg'] = _CMDSTATUSARG
DESCRIPTOR.message_types_by_name['CmdStatusRet'] = _CMDSTATUSRET
DESCRIPTOR.message_types_by_name['CmdStopArg'] = _CMDSTOPARG
DESCRIPTOR.message_types_by_name['CmdStopRet'] = _CMDSTOPRET
DESCRIPTOR.message_types_by_name['CmdRemoveArg'] = _CMDREMOVEARG
DESCRIPTOR.message_types_by_name['CmdRemoveRet'] = _CMDREMOVERET
DESCRIPTOR.message_types_by_name['CmdListArg'] = _CMDLISTARG
DESCRIPTOR.message_types_by_name['CmdListRet'] = _CMDLISTRET
DESCRIPTOR.message_types_by_name['FileGetArg'] = _FILEGETARG
DESCRIPTOR.message_types_by_name['FileGetRet'] = _FILEGETRET

CmdStatus = _reflection.GeneratedProtocolMessageType('CmdStatus', (_message.Message,), dict(
  DESCRIPTOR = _CMDSTATUS,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdStatus)
  ))
_sym_db.RegisterMessage(CmdStatus)

CmdExecuteArg = _reflection.GeneratedProtocolMessageType('CmdExecuteArg', (_message.Message,), dict(
  DESCRIPTOR = _CMDEXECUTEARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdExecuteArg)
  ))
_sym_db.RegisterMessage(CmdExecuteArg)

CmdExecuteRet = _reflection.GeneratedProtocolMessageType('CmdExecuteRet', (_message.Message,), dict(
  DESCRIPTOR = _CMDEXECUTERET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdExecuteRet)
  ))
_sym_db.RegisterMessage(CmdExecuteRet)

CmdStatusArg = _reflection.GeneratedProtocolMessageType('CmdStatusArg', (_message.Message,), dict(
  DESCRIPTOR = _CMDSTATUSARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdStatusArg)
  ))
_sym_db.RegisterMessage(CmdStatusArg)

CmdStatusRet = _reflection.GeneratedProtocolMessageType('CmdStatusRet', (_message.Message,), dict(
  DESCRIPTOR = _CMDSTATUSRET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdStatusRet)
  ))
_sym_db.RegisterMessage(CmdStatusRet)

CmdStopArg = _reflection.GeneratedProtocolMessageType('CmdStopArg', (_message.Message,), dict(
  DESCRIPTOR = _CMDSTOPARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdStopArg)
  ))
_sym_db.RegisterMessage(CmdStopArg)

CmdStopRet = _reflection.GeneratedProtocolMessageType('CmdStopRet', (_message.Message,), dict(
  DESCRIPTOR = _CMDSTOPRET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdStopRet)
  ))
_sym_db.RegisterMessage(CmdStopRet)

CmdRemoveArg = _reflection.GeneratedProtocolMessageType('CmdRemoveArg', (_message.Message,), dict(
  DESCRIPTOR = _CMDREMOVEARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdRemoveArg)
  ))
_sym_db.RegisterMessage(CmdRemoveArg)

CmdRemoveRet = _reflection.GeneratedProtocolMessageType('CmdRemoveRet', (_message.Message,), dict(
  DESCRIPTOR = _CMDREMOVERET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdRemoveRet)
  ))
_sym_db.RegisterMessage(CmdRemoveRet)

CmdListArg = _reflection.GeneratedProtocolMessageType('CmdListArg', (_message.Message,), dict(
  DESCRIPTOR = _CMDLISTARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdListArg)
  ))
_sym_db.RegisterMessage(CmdListArg)

CmdListRet = _reflection.GeneratedProtocolMessageType('CmdListRet', (_message.Message,), dict(

  CmdSummary = _reflection.GeneratedProtocolMessageType('CmdSummary', (_message.Message,), dict(
    DESCRIPTOR = _CMDLISTRET_CMDSUMMARY,
    __module__ = 'charon_agent_interface_pb2'
    # @@protoc_insertion_point(class_scope:nutanix.curie.CmdListRet.CmdSummary)
    ))
  ,
  DESCRIPTOR = _CMDLISTRET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.CmdListRet)
  ))
_sym_db.RegisterMessage(CmdListRet)
_sym_db.RegisterMessage(CmdListRet.CmdSummary)

FileGetArg = _reflection.GeneratedProtocolMessageType('FileGetArg', (_message.Message,), dict(
  DESCRIPTOR = _FILEGETARG,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.FileGetArg)
  ))
_sym_db.RegisterMessage(FileGetArg)

FileGetRet = _reflection.GeneratedProtocolMessageType('FileGetRet', (_message.Message,), dict(
  DESCRIPTOR = _FILEGETRET,
  __module__ = 'charon_agent_interface_pb2'
  # @@protoc_insertion_point(class_scope:nutanix.curie.FileGetRet)
  ))
_sym_db.RegisterMessage(FileGetRet)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))

_CURIEAGENTRPCSVC = _descriptor.ServiceDescriptor(
  name='CurieAgentRpcSvc',
  full_name='nutanix.curie.CurieAgentRpcSvc',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\300\363\030\350\007\310\363\030\024')),
  serialized_start=895,
  serialized_end=1335,
  methods=[
  _descriptor.MethodDescriptor(
    name='CmdExecute',
    full_name='nutanix.curie.CurieAgentRpcSvc.CmdExecute',
    index=0,
    containing_service=None,
    input_type=_CMDEXECUTEARG,
    output_type=_CMDEXECUTERET,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CmdStatus',
    full_name='nutanix.curie.CurieAgentRpcSvc.CmdStatus',
    index=1,
    containing_service=None,
    input_type=_CMDSTATUSARG,
    output_type=_CMDSTATUSRET,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CmdStop',
    full_name='nutanix.curie.CurieAgentRpcSvc.CmdStop',
    index=2,
    containing_service=None,
    input_type=_CMDSTOPARG,
    output_type=_CMDSTOPRET,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CmdRemove',
    full_name='nutanix.curie.CurieAgentRpcSvc.CmdRemove',
    index=3,
    containing_service=None,
    input_type=_CMDREMOVEARG,
    output_type=_CMDREMOVERET,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CmdList',
    full_name='nutanix.curie.CurieAgentRpcSvc.CmdList',
    index=4,
    containing_service=None,
    input_type=_CMDLISTARG,
    output_type=_CMDLISTRET,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FileGet',
    full_name='nutanix.curie.CurieAgentRpcSvc.FileGet',
    index=5,
    containing_service=None,
    input_type=_FILEGETARG,
    output_type=_FILEGETRET,
    options=None,
  ),
])

CurieAgentRpcSvc = service_reflection.GeneratedServiceType('CurieAgentRpcSvc', (_service.Service,), dict(
  DESCRIPTOR = _CURIEAGENTRPCSVC,
  __module__ = 'charon_agent_interface_pb2'
  ))

CurieAgentRpcSvc_Stub = service_reflection.GeneratedServiceStubType('CurieAgentRpcSvc_Stub', (CurieAgentRpcSvc,), dict(
  DESCRIPTOR = _CURIEAGENTRPCSVC,
  __module__ = 'charon_agent_interface_pb2'
  ))


# @@protoc_insertion_point(module_scope)