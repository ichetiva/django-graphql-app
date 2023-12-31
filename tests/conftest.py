import pytest
from django.test.client import Client
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func
