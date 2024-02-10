import pytest

import django.test
import django.urls


@pytest.mark.django_db
def test_product_list() -> None:
    """тестируем список товаров"""
    client = django.test.Client()
    response = client.get(django.urls.reverse_lazy('products:list_create'))
    assert response.status_code == 200
