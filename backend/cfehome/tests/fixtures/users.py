import pytest

import users.models


@pytest.fixture()
def create_superuser() -> users.models.User:
    """создаем тестового суперпользователя"""
    return users.models.User.objects.create_superuser(
        username='superuser1',
        password='password',
        email='super1@ya.ru',
    )


@pytest.fixture()
def create_simple_user1() -> users.models.User:
    """создаем обычного пользователя"""
    return users.models.User.objects.create_user(
        username='user1',
        password='password',
        email='user1@ya.ru',
    )


@pytest.fixture()
def create_simple_user2() -> users.models.User:
    """создаем обычного пользователя"""
    return users.models.User.objects.create_user(
        username='user2',
        password='password',
        email='user2@ya.ru',
    )
