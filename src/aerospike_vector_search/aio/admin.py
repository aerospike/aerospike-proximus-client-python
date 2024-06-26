import asyncio
import logging
import sys
from typing import Any, Optional, Union
import grpc

from .. import types
from .internal import channel_provider
from ..shared.admin_helpers import BaseClient

logger = logging.getLogger(__name__)


class Client(BaseClient):
    """
    Aerospike Vector Search Asyncio Admin Client

    This client is designed to conduct Aerospike Vector Search administrative operation such as creating indexes, querying index information, and dropping indexes.
    """

    def __init__(
        self,
        *,
        seeds: Union[types.HostPort, tuple[types.HostPort, ...]],
        listener_name: Optional[str] = None,
        is_loadbalancer: Optional[bool] = False,
    ) -> None:
        """
        Initialize the Aerospike Vector Search Admin Client.

        Args:
            seeds (Union[types.HostPort, tuple[types.HostPort, ...]]): Used to create appropriate gRPC channels for interacting with Aerospike Vector Search.
            listener_name (Optional[str], optional): Advertised listener for the client. Defaults to None.
            is_loadbalancer (bool, optional): If true, the first seed address will be treated as a load balancer node.

        Raises:
            Exception: Raised when no seed host is provided.

        """
        seeds = self._prepare_seeds(seeds)

        self._channel_provider = channel_provider.ChannelProvider(
            seeds, listener_name, is_loadbalancer
        )

    async def index_create(
        self,
        *,
        namespace: str,
        name: str,
        vector_field: str,
        dimensions: int,
        vector_distance_metric: Optional[types.VectorDistanceMetric] = (
            types.VectorDistanceMetric.SQUARED_EUCLIDEAN
        ),
        sets: Optional[str] = None,
        index_params: Optional[types.HnswParams] = None,
        index_meta_data: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Create an index.

        Args:
            namespace (str): The namespace for the index.
            name (str): The name of the index.
            vector_field (str): The name of the field containing vector data.
            dimensions (int): The number of dimensions in the vector data.
            vector_distance_metric (Optional[types.VectorDistanceMetric], optional):
            The distance metric used to compare when performing a vector search.
            Defaults to VectorDistanceMetric.SQUARED_EUCLIDEAN.
            sets (Optional[str], optional): The set used for the index. Defaults to None.
            index_params (Optional[types.HnswParams], optional):
            Parameters used for tuning vector search. Defaults to None. If index_params is None, then the default values specified for
            types.HnswParams will be used.
            index_meta_data (Optional[dict[str, str]], optional): Meta data associated with the index. Defaults to None.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        Note:
            This method creates an index with the specified parameters and waits for the index creation to complete.
            It waits for up to 100,000 seconds for the index creation to complete.
        """

        await self._channel_provider._is_ready()

        (index_stub, index_create_request) = self._prepare_index_create(
            namespace,
            name,
            vector_field,
            dimensions,
            vector_distance_metric,
            sets,
            index_params,
            index_meta_data,
            logger,
        )

        try:
            await index_stub.Create(index_create_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise types.AVSServerError(rpc_error=e)
        try:
            await self._wait_for_index_creation(
                namespace=namespace, name=name, timeout=100_000
            )
        except grpc.RpcError as e:
            logger.error("Failed waiting for creation with error: %s", e)
            raise types.AVSServerError(rpc_error=e)

    async def index_drop(self, *, namespace: str, name: str) -> None:
        """
        Drop an index.

        Args:
            namespace (str): The namespace of the index.
            name (str): The name of the index.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        Note:
            This method drops an index with the specified parameters and waits for the index deletion to complete.
            It waits for up to 100,000 seconds for the index deletion to complete.
        """
        await self._channel_provider._is_ready()

        (index_stub, index_drop_request) = self._prepare_index_drop(
            namespace, name, logger
        )
        try:
            await index_stub.Drop(index_drop_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise types.AVSServerError(rpc_error=e)
        try:
            await self._wait_for_index_deletion(
                namespace=namespace, name=name, timeout=100_000
            )
        except grpc.RpcError as e:
            logger.error("Failed waiting for deletion with error: %s", e)
            raise types.AVSServerError(rpc_error=e)

    async def index_list(self) -> list[dict]:
        """
        List all indices.

        Returns:
            list[dict]: A list of indices.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.
        """
        await self._channel_provider._is_ready()

        (index_stub, index_list_request) = self._prepare_index_list(logger)
        try:
            response = await index_stub.List(index_list_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise types.AVSServerError(rpc_error=e)
        return self._respond_index_list(response)

    async def index_get(
        self, *, namespace: str, name: str
    ) -> dict[str, Union[int, str]]:
        """
        Retrieve the information related with an index.

        Args:
            namespace (str): The namespace of the index.
            name (str): The name of the index.

        Returns:
            dict[str, Union[int, str]: Information about an index.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        """
        await self._channel_provider._is_ready()

        (index_stub, index_get_request) = self._prepare_index_get(
            namespace, name, logger
        )
        try:
            response = await index_stub.Get(index_get_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise types.AVSServerError(rpc_error=e)
        return self._respond_index_get(response)

    async def index_get_status(self, *, namespace: str, name: str) -> int:
        """
        Retrieve the number of records queued to be merged into an index.

        Args:
            namespace (str): The namespace of the index.
            name (str): The name of the index.

        Returns:
            int: Records queued to be merged into an index.

        Raises:
            grpc.RpcError: Raised if an error occurs during the RPC communication with the server while attempting to create the index.
            This error could occur due to various reasons such as network issues, server-side failures, or invalid request parameters.

        Note:
            This method retrieves the status of the specified index. If index_get_status is called the vector client puts some records into Aerospike Vector Search,
            the records may not immediately begin to merge into the index. To wait for all records to be merged into an index, use vector_client.wait_for_index_completion.

            Warning: This API is subject to change.
        """
        await self._channel_provider._is_ready()

        (index_stub, index_get_status_request) = self._prepare_index_get_status(
            namespace, name, logger
        )
        try:
            response = await index_stub.GetStatus(index_get_status_request)
        except grpc.RpcError as e:
            logger.error("Failed with error: %s", e)
            raise types.AVSServerError(rpc_error=e)

        return self._respond_index_get_status(response)

    async def _wait_for_index_creation(
        self,
        *,
        namespace: str,
        name: str,
        timeout: Optional[int] = sys.maxsize,
        wait_interval: Optional[int] = 0.1,
    ) -> None:
        """
        Wait for the index to be created.
        """
        await self._channel_provider._is_ready()

        (index_stub, wait_interval, start_time, _, _, index_creation_request) = (
            self._prepare_wait_for_index_waiting(namespace, name, wait_interval)
        )
        while True:
            self._check_timeout(start_time, timeout)
            try:
                await index_stub.GetStatus(index_creation_request)
                logger.debug("Index created succesfully")
                # Index has been created
                return
            except grpc.RpcError as e:
                if e.code() in (grpc.StatusCode.UNAVAILABLE, grpc.StatusCode.NOT_FOUND):

                    # Wait for some more time.
                    await asyncio.sleep(wait_interval)
                else:
                    logger.error("Failed with error: %s", e)
                    raise types.AVSServerError(rpc_error=e)

    async def _wait_for_index_deletion(
        self,
        *,
        namespace: str,
        name: str,
        timeout: Optional[int] = sys.maxsize,
        wait_interval: Optional[int] = 0.1,
    ) -> None:
        """
        Wait for the index to be deleted.
        """
        await self._channel_provider._is_ready()

        # Wait interval between polling
        (index_stub, wait_interval, start_time, _, _, index_deletion_request) = (
            self._prepare_wait_for_index_waiting(namespace, name, wait_interval)
        )

        while True:
            self._check_timeout(start_time, timeout)

            try:
                await index_stub.GetStatus(index_deletion_request)
                # Wait for some more time.
                await asyncio.sleep(wait_interval)
            except grpc.RpcError as e:
                if e.code() in (grpc.StatusCode.UNAVAILABLE, grpc.StatusCode.NOT_FOUND):
                    logger.debug("Index deleted succesfully")
                    # Index has been created
                    return
                else:
                    raise types.AVSServerError(rpc_error=e)

    async def close(self):
        """
        Close the Aerospike Vector Search Admin Client.

        This method closes gRPC channels connected to Aerospike Vector Search.

        Note:
            This method should be called when the VectorDbAdminClient is no longer needed to release resources.
        """
        await self._channel_provider.close()

    async def __aenter__(self):
        """
        Enter an asynchronous context manager for the admin client.

        Returns:
            VectorDbAdminlient: Aerospike Vector Search Admin Client instance.
        """
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exit an asynchronous context manager for the admin client.
        """
        await self.close()
