# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x10\x61\x65rospike.vector\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"A\n\x0b\x41uthRequest\x12\x32\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32\x1d.aerospike.vector.Credentials\"\x1d\n\x0c\x41uthResponse\x12\r\n\x05token\x18\x01 \x01(\t2^\n\x0b\x41uthService\x12O\n\x0c\x41uthenticate\x12\x1d.aerospike.vector.AuthRequest\x1a\x1e.aerospike.vector.AuthResponse\"\x00\x42\x43\n!com.aerospike.vector.client.protoP\x01Z\x1c\x61\x65rospike.com/vector/protos/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.aerospike.vector.client.protoP\001Z\034aerospike.com/vector/protos/'
  _globals['_AUTHREQUEST']._serialized_start=74
  _globals['_AUTHREQUEST']._serialized_end=139
  _globals['_AUTHRESPONSE']._serialized_start=141
  _globals['_AUTHRESPONSE']._serialized_end=170
  _globals['_AUTHSERVICE']._serialized_start=172
  _globals['_AUTHSERVICE']._serialized_end=266
# @@protoc_insertion_point(module_scope)
