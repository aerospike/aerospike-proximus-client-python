# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: index.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bindex.proto\x12\x10\x61\x65rospike.vector\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"2\n\x13IndexStatusResponse\x12\x1b\n\x13unmergedRecordCount\x18\x02 \x01(\x03\x32\xf3\x02\n\x0cIndexService\x12\x45\n\x06\x43reate\x12!.aerospike.vector.IndexDefinition\x1a\x16.google.protobuf.Empty\"\x00\x12;\n\x04\x44rop\x12\x19.aerospike.vector.IndexId\x1a\x16.google.protobuf.Empty\"\x00\x12G\n\x04List\x12\x16.google.protobuf.Empty\x1a%.aerospike.vector.IndexDefinitionList\"\x00\x12\x45\n\x03Get\x12\x19.aerospike.vector.IndexId\x1a!.aerospike.vector.IndexDefinition\"\x00\x12O\n\tGetStatus\x12\x19.aerospike.vector.IndexId\x1a%.aerospike.vector.IndexStatusResponse\"\x00\x42=\n\x1b\x63om.aerospike.vector.clientP\x01Z\x1c\x61\x65rospike.com/vector/protos/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.aerospike.vector.clientP\001Z\034aerospike.com/vector/protos/'
  _globals['_INDEXSTATUSRESPONSE']._serialized_start=75
  _globals['_INDEXSTATUSRESPONSE']._serialized_end=125
  _globals['_INDEXSERVICE']._serialized_start=128
  _globals['_INDEXSERVICE']._serialized_end=499
# @@protoc_insertion_point(module_scope)
