# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x10\x61\x65rospike.vector\"\x91\x01\n\x03Key\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x10\n\x03set\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x0bstringValue\x18\x03 \x01(\tH\x00\x12\x14\n\nbytesValue\x18\x04 \x01(\x0cH\x00\x12\x12\n\x08intValue\x18\x05 \x01(\x05H\x00\x12\x13\n\tlongValue\x18\x06 \x01(\x03H\x00\x42\x07\n\x05valueB\x06\n\x04_set\"\x19\n\x08\x42oolData\x12\r\n\x05value\x18\x01 \x03(\x08\"\x1a\n\tFloatData\x12\r\n\x05value\x18\x01 \x03(\x02\"\x94\x01\n\x06MapKey\x12\x15\n\x0bstringValue\x18\x01 \x01(\tH\x00\x12\x14\n\nbytesValue\x18\x02 \x01(\x0cH\x00\x12\x12\n\x08intValue\x18\x03 \x01(\x05H\x00\x12\x13\n\tlongValue\x18\x04 \x01(\x03H\x00\x12\x14\n\nfloatValue\x18\x05 \x01(\x02H\x00\x12\x15\n\x0b\x64oubleValue\x18\x06 \x01(\x01H\x00\x42\x07\n\x05value\"Y\n\x08MapEntry\x12%\n\x03key\x18\x01 \x01(\x0b\x32\x18.aerospike.vector.MapKey\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.aerospike.vector.Value\"2\n\x03Map\x12+\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x1a.aerospike.vector.MapEntry\"0\n\x04List\x12(\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x17.aerospike.vector.Value\"r\n\x06Vector\x12.\n\x08\x62oolData\x18\x01 \x01(\x0b\x32\x1a.aerospike.vector.BoolDataH\x00\x12\x30\n\tfloatData\x18\x02 \x01(\x0b\x32\x1b.aerospike.vector.FloatDataH\x00\x42\x06\n\x04\x64\x61ta\"\xb4\x02\n\x05Value\x12\x15\n\x0bstringValue\x18\x01 \x01(\tH\x00\x12\x14\n\nbytesValue\x18\x02 \x01(\x0cH\x00\x12\x12\n\x08intValue\x18\x03 \x01(\x05H\x00\x12\x13\n\tlongValue\x18\x04 \x01(\x03H\x00\x12\x14\n\nfloatValue\x18\x05 \x01(\x02H\x00\x12\x15\n\x0b\x64oubleValue\x18\x06 \x01(\x01H\x00\x12)\n\x08mapValue\x18\x07 \x01(\x0b\x32\x15.aerospike.vector.MapH\x00\x12+\n\tlistValue\x18\x08 \x01(\x0b\x32\x16.aerospike.vector.ListH\x00\x12/\n\x0bvectorValue\x18\t \x01(\x0b\x32\x18.aerospike.vector.VectorH\x00\x12\x16\n\x0c\x62ooleanValue\x18\n \x01(\x08H\x00\x42\x07\n\x05value\"=\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.aerospike.vector.Value\"A\n\x17\x41\x65rospikeRecordMetadata\x12\x12\n\ngeneration\x18\x01 \x01(\r\x12\x12\n\nexpiration\x18\x02 \x01(\r\"\x85\x01\n\x06Record\x12\'\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x17.aerospike.vector.Field\x12\x46\n\x11\x61\x65rospikeMetadata\x18\x02 \x01(\x0b\x32).aerospike.vector.AerospikeRecordMetadataH\x00\x42\n\n\x08metadata\"z\n\x08Neighbor\x12\"\n\x03key\x18\x01 \x01(\x0b\x32\x15.aerospike.vector.Key\x12-\n\x06record\x18\x02 \x01(\x0b\x32\x18.aerospike.vector.RecordH\x00\x88\x01\x01\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\x42\t\n\x07_record\"*\n\x07IndexId\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xa8\x01\n\nHnswParams\x12\x0e\n\x01m\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x1b\n\x0e\x65\x66\x43onstruction\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x0f\n\x02\x65\x66\x18\x03 \x01(\rH\x02\x88\x01\x01\x12<\n\x0e\x62\x61tchingParams\x18\x04 \x01(\x0b\x32$.aerospike.vector.HnswBatchingParamsB\x04\n\x02_mB\x11\n\x0f_efConstructionB\x05\n\x03_ef\"*\n\x10HnswSearchParams\x12\x0f\n\x02\x65\x66\x18\x01 \x01(\rH\x00\x88\x01\x01\x42\x05\n\x03_ef\"\x84\x01\n\x12HnswBatchingParams\x12\x17\n\nmaxRecords\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x15\n\x08interval\x18\x02 \x01(\rH\x01\x88\x01\x01\x12\x15\n\x08\x64isabled\x18\x03 \x01(\x08H\x02\x88\x01\x01\x42\r\n\x0b_maxRecordsB\x0b\n\t_intervalB\x0b\n\t_disabled\"N\n\x0cIndexStorage\x12\x16\n\tnamespace\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03set\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x0c\n\n_namespaceB\x06\n\x04_set\"\xe0\x03\n\x0fIndexDefinition\x12%\n\x02id\x18\x01 \x01(\x0b\x32\x19.aerospike.vector.IndexId\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.aerospike.vector.IndexType\x12\x12\n\ndimensions\x18\x03 \x01(\r\x12\x44\n\x14vectorDistanceMetric\x18\x04 \x01(\x0e\x32&.aerospike.vector.VectorDistanceMetric\x12\r\n\x05\x66ield\x18\x05 \x01(\t\x12\x16\n\tsetFilter\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x32\n\nhnswParams\x18\x07 \x01(\x0b\x32\x1c.aerospike.vector.HnswParamsH\x00\x12=\n\x06labels\x18\x08 \x03(\x0b\x32-.aerospike.vector.IndexDefinition.LabelsEntry\x12\x34\n\x07storage\x18\t \x01(\x0b\x32\x1e.aerospike.vector.IndexStorageH\x02\x88\x01\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x06paramsB\x0c\n\n_setFilterB\n\n\x08_storage\"I\n\x13IndexDefinitionList\x12\x32\n\x07indices\x18\x01 \x03(\x0b\x32!.aerospike.vector.IndexDefinition\"\x18\n\x07\x42oolean\x12\r\n\x05value\x18\x01 \x01(\x08*f\n\x14VectorDistanceMetric\x12\x15\n\x11SQUARED_EUCLIDEAN\x10\x00\x12\n\n\x06\x43OSINE\x10\x01\x12\x0f\n\x0b\x44OT_PRODUCT\x10\x02\x12\r\n\tMANHATTAN\x10\x03\x12\x0b\n\x07HAMMING\x10\x04*\x15\n\tIndexType\x12\x08\n\x04HNSW\x10\x00\x42=\n\x1b\x63om.aerospike.vector.clientP\x01Z\x1c\x61\x65rospike.com/vector/protos/b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.aerospike.vector.clientP\001Z\034aerospike.com/vector/protos/'
  _globals['_INDEXDEFINITION_LABELSENTRY']._options = None
  _globals['_INDEXDEFINITION_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_VECTORDISTANCEMETRIC']._serialized_start=2455
  _globals['_VECTORDISTANCEMETRIC']._serialized_end=2557
  _globals['_INDEXTYPE']._serialized_start=2559
  _globals['_INDEXTYPE']._serialized_end=2580
  _globals['_KEY']._serialized_start=34
  _globals['_KEY']._serialized_end=179
  _globals['_BOOLDATA']._serialized_start=181
  _globals['_BOOLDATA']._serialized_end=206
  _globals['_FLOATDATA']._serialized_start=208
  _globals['_FLOATDATA']._serialized_end=234
  _globals['_MAPKEY']._serialized_start=237
  _globals['_MAPKEY']._serialized_end=385
  _globals['_MAPENTRY']._serialized_start=387
  _globals['_MAPENTRY']._serialized_end=476
  _globals['_MAP']._serialized_start=478
  _globals['_MAP']._serialized_end=528
  _globals['_LIST']._serialized_start=530
  _globals['_LIST']._serialized_end=578
  _globals['_VECTOR']._serialized_start=580
  _globals['_VECTOR']._serialized_end=694
  _globals['_VALUE']._serialized_start=697
  _globals['_VALUE']._serialized_end=1005
  _globals['_FIELD']._serialized_start=1007
  _globals['_FIELD']._serialized_end=1068
  _globals['_AEROSPIKERECORDMETADATA']._serialized_start=1070
  _globals['_AEROSPIKERECORDMETADATA']._serialized_end=1135
  _globals['_RECORD']._serialized_start=1138
  _globals['_RECORD']._serialized_end=1271
  _globals['_NEIGHBOR']._serialized_start=1273
  _globals['_NEIGHBOR']._serialized_end=1395
  _globals['_INDEXID']._serialized_start=1397
  _globals['_INDEXID']._serialized_end=1439
  _globals['_HNSWPARAMS']._serialized_start=1442
  _globals['_HNSWPARAMS']._serialized_end=1610
  _globals['_HNSWSEARCHPARAMS']._serialized_start=1612
  _globals['_HNSWSEARCHPARAMS']._serialized_end=1654
  _globals['_HNSWBATCHINGPARAMS']._serialized_start=1657
  _globals['_HNSWBATCHINGPARAMS']._serialized_end=1789
  _globals['_INDEXSTORAGE']._serialized_start=1791
  _globals['_INDEXSTORAGE']._serialized_end=1869
  _globals['_INDEXDEFINITION']._serialized_start=1872
  _globals['_INDEXDEFINITION']._serialized_end=2352
  _globals['_INDEXDEFINITION_LABELSENTRY']._serialized_start=2271
  _globals['_INDEXDEFINITION_LABELSENTRY']._serialized_end=2316
  _globals['_INDEXDEFINITIONLIST']._serialized_start=2354
  _globals['_INDEXDEFINITIONLIST']._serialized_end=2427
  _globals['_BOOLEAN']._serialized_start=2429
  _globals['_BOOLEAN']._serialized_end=2453
# @@protoc_insertion_point(module_scope)
