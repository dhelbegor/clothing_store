import pytest
from pytest_factoryboy import register
from django.contrib.auth import get_user_model
from apps.stock.tests.factories import ProductFactory, ProductManagementFactory

register(ProductFactory)
register(ProductManagementFactory)


@pytest.fixture
def user():
    klass = get_user_model()
    user = klass.objects.create(email='testuser@stock.com')
    return user


@pytest.fixture
def auth_client(user, client):
    client.force_login(user)
    return client


@pytest.fixture
def headers():
    """default headers on make request"""
    return {'content_type': "application/json"}
