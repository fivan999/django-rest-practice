import pytest

import users.models


@pytest.fixture()
def create_superuser() -> None:
    """создаем тестового суперпользователя"""
    users.models.User.objects.create_superuser(
        username='superuser1',
        password='password',
        email='super1@ya.ru',
    )


@pytest.fixture()
def create_simple_user() -> None:
    """создаем обычного пользователя"""
    users.models.User.objects.create_user(
        username='user1',
        password='password',
        email='user1@ya.ru',
    )
