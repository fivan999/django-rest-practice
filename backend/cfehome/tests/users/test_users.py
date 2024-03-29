import pytest
import rest_framework.test

import django.urls


@pytest.mark.parametrize(
    ('username', 'password', 'result'),
    [
        ('user1', 'password', True),
        ('superuser1', 'password', True),
        ('not exist', 'pass', False),
    ],
)
@pytest.mark.django_db
def test_login_via_jwt(
    create_superuser,
    create_simple_user1,
    username: str,
    password: str,
    result: bool,
) -> None:
    """тестируем вход в аккаунт"""
    client = rest_framework.test.APIClient()
    response = client.post(
        django.urls.reverse_lazy('auth:token_obtain'),
        data={'username': username, 'password': password},
    )
    assert (response.status_code == 200) == result
    assert ('access' in response.data) == result
    assert ('refresh' in response.data) == result
