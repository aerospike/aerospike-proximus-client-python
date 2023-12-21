# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transact.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etransact.proto\x12\x10\x61\x65rospike.vector\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"U\n\nPutRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12#\n\x04\x62ins\x18\x03 \x03(\x0b\x32\x15.aerospike.vector.Bin\"d\n\nGetRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12\x32\n\x0b\x62inSelector\x18\x02 \x01(\x0b\x32\x1d.aerospike.vector.BinSelector\"P\n\x0b\x42inSelector\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.aerospike.vector.BinSelectorType\x12\x10\n\x08\x62inNames\x18\x02 \x03(\t\"\x81\x02\n\x13VectorSearchRequest\x12(\n\x05index\x18\x01 \x01(\x0b\x32\x19.aerospike.vector.IndexId\x12-\n\x0bqueryVector\x18\x02 \x01(\x0b\x32\x18.aerospike.vector.Vector\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x32\n\x0b\x62inSelector\x18\x04 \x01(\x0b\x32\x1d.aerospike.vector.BinSelector\x12>\n\x10hnswSearchParams\x18\x05 \x01(\x0b\x32\".aerospike.vector.HnswSearchParamsH\x00\x42\x0e\n\x0csearchParams*3\n\x0f\x42inSelectorType\x12\x07\n\x03\x41LL\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\r\n\tSPECIFIED\x10\x02\x32\xa4\x02\n\x08Transact\x12=\n\x03Put\x12\x1c.aerospike.vector.PutRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x03Get\x12\x1c.aerospike.vector.GetRequest\x1a\x18.aerospike.vector.Record\"\x00\x12<\n\x06\x45xists\x12\x15.aerospike.vector.Key\x1a\x19.aerospike.vector.Boolean\"\x00\x12Z\n\x0cVectorSearch\x12%.aerospike.vector.VectorSearchRequest\x1a\x1f.aerospike.vector.RecordWithKey\"\x00\x30\x01\x42=\n\x1b\x63om.aerospike.vector.clientP\x01Z\x1c\x61\x65rospike.com/vector/protos/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transact_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.aerospike.vector.clientP\001Z\034aerospike.com/vector/protos/'
  _globals['_BINSELECTORTYPE']._serialized_start=609
  _globals['_BINSELECTORTYPE']._serialized_end=660
  _globals['_PUTREQUEST']._serialized_start=78
  _globals['_PUTREQUEST']._serialized_end=163
  _globals['_GETREQUEST']._serialized_start=165
  _globals['_GETREQUEST']._serialized_end=265
  _globals['_BINSELECTOR']._serialized_start=267
  _globals['_BINSELECTOR']._serialized_end=347
  _globals['_VECTORSEARCHREQUEST']._serialized_start=350
  _globals['_VECTORSEARCHREQUEST']._serialized_end=607
  _globals['_TRANSACT']._serialized_start=663
  _globals['_TRANSACT']._serialized_end=955
# @@protoc_insertion_point(module_scope)
