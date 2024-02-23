import pytest

import django.urls

import tests.utils.utils


@pytest.fixture
def create_public_product(create_simple_user1) -> int:
    """создаем тестовый публичный товар и возвращаем его id"""
    client = tests.utils.utils.get_test_client('user1')
    response = client.post(
        django.urls.reverse_lazy('products:product-list'),
        data={'title': 'product1', 'description': 'test1', 'price': 1},
    )
    return response.data['pk']


@pytest.fixture
def create_private_product(create_simple_user1) -> int:
    """создаем тестовый приватный товар и возвращаем его id"""
    client = tests.utils.utils.get_test_client('user1')
    response = client.post(
        django.urls.reverse_lazy('products:product-list'),
        data={
            'title': 'product2',
            'description': 'test2',
            'price': 1,
            'is_public': False,
        },
    )
    return response.data['pk']
