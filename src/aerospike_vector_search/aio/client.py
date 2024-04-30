import asyncio
import logging
import sys
from typing import Any, Optional, Union

import grpc

from .. import types
from .internal import channel_provider
from ..shared.client_helpers import BaseClient

logger = logging.getLogger(__name__)

class Client(BaseClient):
    """
    Aerospike Vector Search Asyncio Admin Client

    This client specializes in performing database operations with vector data.
    Moreover, the client supports Hierarchical Navigable Small World (HNSW) vector searches,
    allowing users to find vectors similar to a given query vector within an index.
    """

    def __init__(
        self,
        *,
        seeds: Union[types.HostPort, tuple[types.HostPort, ...]],
        listener_name: Optional[str] = None,
        is_loadbalancer: Optional[bool] = False,
    ) -> None:
        """
        Initialize the Aerospike Vector Search Vector Client.

        Args:
            seeds (Union[types.HostPort, tuple[types.HostPort, ...]]):
                Used to create appropriate gRPC channels for interacting with Aerospike Vector Search.
            listener_name (Optional[str], optional):
                Advertised listener for the client. Defaults to None.
            is_loadbalancer (bool, optional):
                If true, the first seed address will be treated as a load balancer node.

        Raises:
            Exception: Raised when no seed host is provided.
        """
        seeds = self.prepare_seeds(seeds)
        self._channelProvider = channel_provider.ChannelProvider(
            seeds, listener_name, is_loadbalancer
        )

    async def put(
        self,
        *,
        namespace: str,
        key: Union[int, str, bytes, bytearray],
        record_data: dict[str, Any],
        set_name: Optional[str] = None,
    ) -> None:
        """
        Write a record to Aerospike Vector Search.

        Args:
            namespace (str): The namespace for the record.
            key (Union[int, str, bytes, bytearray]): The key for the record.
            record_data (dict[str, Any]): The data to be stored in the record.
            set_name (Optional[str], optional): The name of the set to which the record belongs. Defaults to None.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        """
        (transact_stub, put_request) = self.prepare_put(namespace, key, record_data, set_name, logger)

        try:
            await transact_stub.Put(put_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise e

    async def get(
        self,
        *,
        namespace: str,
        key: Union[int, str, bytes, bytearray],
        bin_names: Optional[list[str]] = None,
        set_name: Optional[str] = None,
    ) -> types.RecordWithKey:
        """
        Read a record from Aerospike Vector Search.

        Args:
            namespace (str): The namespace for the record.
            key (Union[int, str, bytes, bytearray]): The key for the record.
            bin_names (Optional[list[str]], optional): A list of bin names to retrieve from the record.
            If None, all bins are retrieved. Defaults to None.
            set_name (Optional[str], optional): The name of the set from which to read the record. Defaults to None.

        Returns:
            types.RecordWithKey: A record with its associated key.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.
        """
        (transact_stub, key, get_request) = self.prepare_get(namespace, key, bin_names, set_name, logger)
        try:
            response = await transact_stub.Get(get_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise e

        return self.respond_get(response, key)

    async def exists(
        self, *, namespace: str, key: Any, set_name: Optional[str] = None
    ) -> bool:
        """
        Check if a record exists in Aerospike Vector Search.

        Args:
            namespace (str): The namespace for the record.
            key (Any): The key for the record.
            set_name (Optional[str], optional): The name of the set to which the record belongs. Defaults to None.

        Returns:
            bool: True if the record exists, False otherwise.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.
        """
        (transact_stub, key) = self.prepare_exists(namespace, key, set_name, logger)
        try:
            response = await transact_stub.Exists(key)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise e

        return self.respond_exists(response)

    async def is_indexed(
        self,
        *,
        namespace: str,
        key: Union[int, str, bytes, bytearray],
        index_name: str,
        index_namespace: Optional[str] = None,
        set_name: Optional[str] = None,
    ) -> bool:
        """
        Check if a record is indexed in the Vector DB.

        Args:
            namespace (str): The namespace for the record.
            key (Union[int, str, bytes, bytearray]): The key for the record.
            index_name (str): The name of the index.
            index_namespace (Optional[str], optional): The namespace of the index.
            If None, defaults to the namespace of the record. Defaults to None.
            set_name (Optional[str], optional): The name of the set to which the record belongs. Defaults to None.

        Returns:
            bool: True if the record is indexed, False otherwise.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.
        """
        (transact_stub, is_indexed_request) = self.prepare_is_indexed(namespace, key, index_name, index_namespace, set_name, logger)
        try:
            response = await transact_stub.IsIndexed(is_indexed_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise e
        return self.respond_is_indexed(response)

    async def vector_search(
        self,
        *,
        namespace: str,
        index_name: str,
        query: list[Union[bool, float]],
        limit: int,
        search_params: Optional[types.HnswSearchParams] = None,
        bin_names: Optional[list[str]] = None,
    ) -> list[types.Neighbor]:
        """
        Perform a Hierarchical Navigable Small World (HNSW) vector search in Aerospike Vector Search.

        Args:
            namespace (str): The namespace for the records.
            index_name (str): The name of the index.
            query (list[Union[bool, float]]): The query vector for the search.
            limit (int): The maximum number of neighbors to return. K value.
            search_params (Optional[types_pb2.HnswSearchParams], optional): Parameters for the HNSW algorithm.
            If None, the default parameters for the index are used. Defaults to None.
            bin_names (Optional[list[str]], optional): A list of bin names to retrieve from the results.
            If None, all bins are retrieved. Defaults to None.

        Returns:
            list[types.Neighbor]: A list of neighbors records found by the search.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.
        """
        (transact_stub, vector_search_request) = self.prepare_vector_search(namespace, index_name, query, limit, search_params, bin_names, logger)

        try:
            results_stream = transact_stub.VectorSearch(vector_search_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise e
        async_results = []
        async for result in results_stream:
            async_results.append(self.respond_neighbor(result))

        return async_results

    async def wait_for_index_completion(
        self, *, namespace: str, name: str, timeout: Optional[int] = sys.maxsize
    ) -> None:
        """
        Wait for the index to have no pending index update operations.

        Args:
            namespace (str): The namespace of the index.
            name (str): The name of the index.
            timeout (int, optional): The maximum time (in seconds) to wait for the index to complete.
            Defaults to sys.maxsize.

        Raises:
            Exception: Raised when the timeout occurs while waiting for index completion.
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        Note:
            The function polls the index status with a wait interval of 10 seconds until either
            the timeout is reached or the index has no pending index update operations.
        """
        # Wait interval between polling
        (index_stub, wait_interval, start_time, unmerged_record_initialized, double_check, index_completion_request) = self.prepare_wait_for_index_waiting(namespace, name)
        while True:
            try:
                index_status = await index_stub.GetStatus(index_completion_request)

            except grpc.RpcError as e:
                if e.code() == grpc.StatusCode.UNAVAILABLE:
                    continue
                else:
                    logger.error("Failed with error: %s", e)
                    raise e
            if self.check_completion_condition(start_time, timeout, index_status, unmerged_record_initialized):
                if double_check:
                    return
                else:
                    double_check = True
            else:
                double_check = False
            await asyncio.sleep(wait_interval)

    async def close(self):
        """
        Close the Aerospike Vector Search Vector Client.

        This method closes gRPC channels connected to Aerospike Vector Search.

        Note:
            This method should be called when the VectorDbAdminClient is no longer needed to release resources.
        """
        await self._channelProvider.close()

    async def __aenter__(self):
        """
        Enter an asynchronous context manager for the vector client.

        Returns:
            VectorDbClient: Aerospike Vector Search Vector Client instance.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exit an asynchronous context manager for the vector client.
        """
        await self.close()