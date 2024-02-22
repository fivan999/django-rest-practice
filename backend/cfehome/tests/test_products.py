import pytest

import django.test
import django.urls

import products.models


@pytest.mark.django_db
def test_product_list() -> None:
    """тестируем список товаров"""
    client = django.test.Client()
    response = client.get(django.urls.reverse_lazy('products:product-list'))
    assert response.status_code == 200


@pytest.mark.parametrize(
    ('username', 'password', 'result'),
    [
        ('user1', 'password', True),
        ('superuser1', 'password', True),
        ('not_exist', 'pass', False),
    ],
)
@pytest.mark.django_db(transaction=True)
def test_create_product(
    create_simple_user,
    create_superuser,
    username: str,
    password: str,
    result: bool,
) -> None:
    """тестируем создание товара разными пользователями"""
    client = django.test.Client()
    # вход через определенного пользователя
    login_response = client.post(
        django.urls.reverse_lazy('auth:token_obtain'),
        data={'username': username, 'password': password},
    )
    access_token = login_response.data.get('access', '')

    # создание товара
    create_response = client.post(
        django.urls.reverse_lazy('products:product-list'),
        data={'title': 'product', 'description': 'desc', 'price': 1},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert (create_response.status_code == 201) == result
    assert (products.models.Product.objects.count() == 1) == result
