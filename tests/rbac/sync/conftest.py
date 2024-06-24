import pytest

from aerospike_vector_search import Client
from aerospike_vector_search.admin import Client as AdminClient
from aerospike_vector_search import types


@pytest.fixture(scope="module", autouse=True)
def drop_all_indexes(username, password, root_certificate, host, port):
    with AdminClient(
        seeds=types.HostPort(host=host, port=port), username=username, password=password, root_certificate=root_certificate
    ) as client:
        index_list = client.index_list()

        tasks = []
        for item in index_list:
            client.index_drop(namespace="test", name=item['id']['name'])


@pytest.fixture(scope="module")
def session_rbac_admin_client(username, password, root_certificate, host, port):
    client = AdminClient(
        seeds=types.HostPort(host=host, port=port), username=username, password=password, root_certificate=root_certificate,
    )
    yield client
    client.close()



