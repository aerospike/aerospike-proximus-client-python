.. aerospike-vector documentation master file, created by
   sphinx-quickstart on Thu Apr 11 07:35:51 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Aerospike Vector Client for Python.

This package splits the client functionality into two separate clients.

This vector client (VectorDbClient) specializes in performing database operations with vector data.
Moreover, the client supports Hierarchical Navigable Small World (HNSW) vector searches,
allowing users to find vectors similar to a given query vector within an index.

This admin client (VectorDbAdminClient) is designed to conduct Proximus administrative operation such
as creating indexes, querying index information, and dropping indexes.

Please explore the modules below for more information on API usage and details.

============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   vectordb_client
   vectordb_admin
   types

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`