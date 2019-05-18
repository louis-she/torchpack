# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: minetorch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='minetorch.proto',
  package='minetorch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fminetorch.proto\x12\tminetorch\"x\n\nHeyMessage\x12\x0f\n\x07ip_addr\x18\x01 \x01(\t\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.minetorch.HeyMessage.Status\"+\n\x06Status\x12\x08\n\x04IDLE\x10\x00\x12\x0c\n\x08TRAINING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\"\x1a\n\tYoMessage\x12\r\n\x05roger\x18\x01 \x01(\x08\x32\x43\n\tMinetorch\x12\x36\n\x05HeyYo\x12\x15.minetorch.HeyMessage\x1a\x14.minetorch.YoMessage\"\x00\x62\x06proto3')
)



_HEYMESSAGE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='minetorch.HeyMessage.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRAINING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=107,
  serialized_end=150,
)
_sym_db.RegisterEnumDescriptor(_HEYMESSAGE_STATUS)


_HEYMESSAGE = _descriptor.Descriptor(
  name='HeyMessage',
  full_name='minetorch.HeyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_addr', full_name='minetorch.HeyMessage.ip_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='minetorch.HeyMessage.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEYMESSAGE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=150,
)


_YOMESSAGE = _descriptor.Descriptor(
  name='YoMessage',
  full_name='minetorch.YoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roger', full_name='minetorch.YoMessage.roger', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=178,
)

_HEYMESSAGE.fields_by_name['status'].enum_type = _HEYMESSAGE_STATUS
_HEYMESSAGE_STATUS.containing_type = _HEYMESSAGE
DESCRIPTOR.message_types_by_name['HeyMessage'] = _HEYMESSAGE
DESCRIPTOR.message_types_by_name['YoMessage'] = _YOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeyMessage = _reflection.GeneratedProtocolMessageType('HeyMessage', (_message.Message,), dict(
  DESCRIPTOR = _HEYMESSAGE,
  __module__ = 'minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.HeyMessage)
  ))
_sym_db.RegisterMessage(HeyMessage)

YoMessage = _reflection.GeneratedProtocolMessageType('YoMessage', (_message.Message,), dict(
  DESCRIPTOR = _YOMESSAGE,
  __module__ = 'minetorch_pb2'
  # @@protoc_insertion_point(class_scope:minetorch.YoMessage)
  ))
_sym_db.RegisterMessage(YoMessage)



_MINETORCH = _descriptor.ServiceDescriptor(
  name='Minetorch',
  full_name='minetorch.Minetorch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=180,
  serialized_end=247,
  methods=[
  _descriptor.MethodDescriptor(
    name='HeyYo',
    full_name='minetorch.Minetorch.HeyYo',
    index=0,
    containing_service=None,
    input_type=_HEYMESSAGE,
    output_type=_YOMESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MINETORCH)

DESCRIPTOR.services_by_name['Minetorch'] = _MINETORCH

# @@protoc_insertion_point(module_scope)
