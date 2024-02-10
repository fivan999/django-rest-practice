import pytest

import django.test
import django.urls


@pytest.mark.django_db
def test_success_login() -> None:
    """тестируем успешный вход в аккаунт"""
    client = django.test.Client()
    response = client.post(
        django.urls.reverse_lazy('auth:login'),
        data={'username': 'bebra_dev', 'password': 'easy12345'},
    )
    assert response.status_code == 200
