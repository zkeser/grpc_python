# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\"H\n\x0f\x44\x65layedResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12$\n\x07request\x18\x02 \x03(\x0b\x32\x13.greet.HelloRequest\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8b\x02\n\x07Greeter\x12\x35\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x14.greet.HelloResponse\x12>\n\x0fParrotSaysHello\x12\x13.greet.HelloRequest\x1a\x14.greet.HelloResponse0\x01\x12\x46\n\x15\x43hattyClientSaysHello\x12\x13.greet.HelloRequest\x1a\x16.greet.DelayedResponse(\x01\x12\x41\n\x10InteractingHello\x12\x13.greet.HelloRequest\x1a\x14.greet.HelloResponse(\x01\x30\x01\x62\x06proto3')



_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_DELAYEDRESPONSE = DESCRIPTOR.message_types_by_name['DelayedResponse']
_HELLORESPONSE = DESCRIPTOR.message_types_by_name['HelloResponse']
HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

DelayedResponse = _reflection.GeneratedProtocolMessageType('DelayedResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELAYEDRESPONSE,
  '__module__' : 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.DelayedResponse)
  })
_sym_db.RegisterMessage(DelayedResponse)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.HelloResponse)
  })
_sym_db.RegisterMessage(HelloResponse)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=22
  _HELLOREQUEST._serialized_end=68
  _DELAYEDRESPONSE._serialized_start=70
  _DELAYEDRESPONSE._serialized_end=142
  _HELLORESPONSE._serialized_start=144
  _HELLORESPONSE._serialized_end=176
  _GREETER._serialized_start=179
  _GREETER._serialized_end=446
# @@protoc_insertion_point(module_scope)
