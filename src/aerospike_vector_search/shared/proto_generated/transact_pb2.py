# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transact.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etransact.proto\x12\x10\x61\x65rospike.vector\x1a\x1bgoogle/protobuf/empty.proto\x1a\x0btypes.proto\"\x89\x01\n\nPutRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12.\n\twriteType\x18\x02 \x01(\x0e\x32\x1b.aerospike.vector.WriteType\x12\'\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x17.aerospike.vector.Field\"j\n\nGetRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12\x38\n\x0eprojectionSpec\x18\x02 \x01(\x0b\x32 .aerospike.vector.ProjectionSpec\"3\n\rExistsRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\"3\n\rDeleteRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\"b\n\x10IsIndexedRequest\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12*\n\x07indexId\x18\x02 \x01(\x0b\x32\x19.aerospike.vector.IndexId\"R\n\x10ProjectionFilter\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .aerospike.vector.ProjectionType\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\"z\n\x0eProjectionSpec\x12\x33\n\x07include\x18\x01 \x01(\x0b\x32\".aerospike.vector.ProjectionFilter\x12\x33\n\x07\x65xclude\x18\x02 \x01(\x0b\x32\".aerospike.vector.ProjectionFilter\"\x83\x02\n\x13VectorSearchRequest\x12(\n\x05index\x18\x01 \x01(\x0b\x32\x19.aerospike.vector.IndexId\x12-\n\x0bqueryVector\x18\x02 \x01(\x0b\x32\x18.aerospike.vector.Vector\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x34\n\nprojection\x18\x04 \x01(\x0b\x32 .aerospike.vector.ProjectionSpec\x12>\n\x10hnswSearchParams\x18\x05 \x01(\x0b\x32\".aerospike.vector.HnswSearchParamsH\x00\x42\x0e\n\x0csearchParams*X\n\tWriteType\x12\n\n\x06UPSERT\x10\x00\x12\x0f\n\x0bUPDATE_ONLY\x10\x01\x12\x0f\n\x0bINSERT_ONLY\x10\x02\x12\x0b\n\x07REPLACE\x10\x03\x12\x10\n\x0cREPLACE_ONLY\x10\x04*2\n\x0eProjectionType\x12\x07\n\x03\x41LL\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\r\n\tSPECIFIED\x10\x02\x32\xbc\x03\n\x08Transact\x12=\n\x03Put\x12\x1c.aerospike.vector.PutRequest\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x03Get\x12\x1c.aerospike.vector.GetRequest\x1a\x18.aerospike.vector.Record\"\x00\x12\x43\n\x06\x44\x65lete\x12\x1f.aerospike.vector.DeleteRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x46\n\x06\x45xists\x12\x1f.aerospike.vector.ExistsRequest\x1a\x19.aerospike.vector.Boolean\"\x00\x12L\n\tIsIndexed\x12\".aerospike.vector.IsIndexedRequest\x1a\x19.aerospike.vector.Boolean\"\x00\x12U\n\x0cVectorSearch\x12%.aerospike.vector.VectorSearchRequest\x1a\x1a.aerospike.vector.Neighbor\"\x00\x30\x01\x42\x43\n!com.aerospike.vector.client.protoP\x01Z\x1c\x61\x65rospike.com/vector/protos/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transact_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.aerospike.vector.client.protoP\001Z\034aerospike.com/vector/protos/'
  _globals['_WRITETYPE']._serialized_start=1002
  _globals['_WRITETYPE']._serialized_end=1090
  _globals['_PROJECTIONTYPE']._serialized_start=1092
  _globals['_PROJECTIONTYPE']._serialized_end=1142
  _globals['_PUTREQUEST']._serialized_start=79
  _globals['_PUTREQUEST']._serialized_end=216
  _globals['_GETREQUEST']._serialized_start=218
  _globals['_GETREQUEST']._serialized_end=324
  _globals['_EXISTSREQUEST']._serialized_start=326
  _globals['_EXISTSREQUEST']._serialized_end=377
  _globals['_DELETEREQUEST']._serialized_start=379
  _globals['_DELETEREQUEST']._serialized_end=430
  _globals['_ISINDEXEDREQUEST']._serialized_start=432
  _globals['_ISINDEXEDREQUEST']._serialized_end=530
  _globals['_PROJECTIONFILTER']._serialized_start=532
  _globals['_PROJECTIONFILTER']._serialized_end=614
  _globals['_PROJECTIONSPEC']._serialized_start=616
  _globals['_PROJECTIONSPEC']._serialized_end=738
  _globals['_VECTORSEARCHREQUEST']._serialized_start=741
  _globals['_VECTORSEARCHREQUEST']._serialized_end=1000
  _globals['_TRANSACT']._serialized_start=1145
  _globals['_TRANSACT']._serialized_end=1589
# @@protoc_insertion_point(module_scope)
