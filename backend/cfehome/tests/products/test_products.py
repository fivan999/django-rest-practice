import pytest
import rest_framework.test

import django.urls

import products.models
import tests.utils.utils


@pytest.mark.django_db
def test_product_list() -> None:
    """тестируем список товаров"""
    client = rest_framework.test.APIClient()
    response = client.get(django.urls.reverse_lazy('products:product-list'))
    assert response.status_code == 200


@pytest.mark.parametrize(
    ('username', 'result'),
    [
        ('user1', True),
        ('superuser1', True),
        ('not_exist', False),
    ],
)
@pytest.mark.django_db(transaction=True)
def test_create_product(
    create_simple_user1,
    create_superuser,
    username: str,
    result: bool,
) -> None:
    """тестируем создание товара разными пользователями"""
    client = tests.utils.utils.get_test_client(username)
    # создание товара
    create_response = client.post(
        django.urls.reverse_lazy('products:product-list'),
        data={'title': 'product', 'description': 'desc', 'price': 1},
    )
    assert (create_response.status_code == 201) == result
    assert (products.models.Product.objects.count() == 1) == result


@pytest.mark.parametrize(
    ('username', 'result'),
    [
        ('user1', True),  # собственник товара
        ('user2', True),  # левый чувак
        ('superuser1', True),  # суперпользователь
        ('not_exist', False),  # аноним
    ],
)
@pytest.mark.django_db()
def test_public_product_access(
    create_superuser,
    create_simple_user2,
    create_public_product,
    username: str,
    result: bool,
) -> None:
    """тестируем доступ к публичному товару разными пользователями"""
    client = tests.utils.utils.get_test_client(username)
    response = client.get(
        django.urls.reverse_lazy(
            'products:product-detail', args=(create_public_product,)
        ),
    )
    assert (response.status_code == 200) == result


@pytest.mark.parametrize(
    ('username', 'result'),
    [
        ('user1', True),  # собственник товара
        ('user2', False),  # левый чувак
        ('superuser1', True),  # суперпользователь
        ('not_exist', False),  # аноним
    ],
)
@pytest.mark.django_db()
def test_private_product_access(
    create_superuser,
    create_simple_user2,
    create_private_product,
    username: str,
    result: bool,
) -> None:
    """тестируем доступ к приватному товару разными пользователями"""
    client = tests.utils.utils.get_test_client(username)
    response = client.get(
        django.urls.reverse_lazy(
            'products:product-detail', args=(create_private_product,)
        ),
    )
    assert (response.status_code == 200) == result
