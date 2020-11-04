import uuid
from decimal import Decimal

from django.urls import reverse
from rest_framework import status


def test_list_product(db, auth_client, product):
    url = reverse('api:stock:products-list-create')
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_delete_product(db, auth_client, product):
    url = reverse('api:stock:products-retrieve', kwargs={'pk': product.id})
    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_detail_product(db, auth_client, product):
    url = reverse('api:stock:products-retrieve', kwargs={'pk': product.id})
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_partial_update_product(db, auth_client, product, headers):
    url = reverse('api:stock:products-retrieve', kwargs={'pk': product.id})
    payload = {
        'name': 'Camiseta Aramis Logo Azul'
    }
    response = auth_client.patch(url, payload, **headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_create_product(db, auth_client, product):
    url = reverse('api:stock:products-list-create')
    payload = {
        'name': product.name,
        'sku': uuid.uuid4(),
        'quantity': product.quantity,
        'image_url': product.image_url,
        'category': product.category,
        'size': product.size,
        'price': product.price
    }
    response = auth_client.post(url, payload)
    results = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert results['id']


def test_list_product_management(db, auth_client, product_management):
    url = reverse('api:stock:products-management-list-create')
    response = auth_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_create_product_management(db, auth_client, product_management):
    url = reverse('api:stock:products-management-list-create')
    payload = {
        'product': product_management.product.id,
        'sell_per_day': product_management.sell_per_day,
        'month': product_management.month,
        'total_sell': product_management.total_sell
    }
    response = auth_client.post(url, payload)
    results = response.json()
    assert response.status_code == status.HTTP_201_CREATED
    assert results['id']


def test_partial_update_product_management(db, auth_client, product_management, headers):
    url = reverse('api:stock:products-management-retrieve', kwargs={'pk': product_management.product.id})
    payload = {
        'sell_per_day': 10
    }
    response = auth_client.patch(url, payload, **headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_delete_product_management(db, auth_client, product_management):
    url = reverse('api:stock:products-management-retrieve', kwargs={'pk': product_management.product.id})
    response = auth_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
