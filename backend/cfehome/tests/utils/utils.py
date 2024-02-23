import typing

import rest_framework.test
import rest_framework_simplejwt.tokens

import users.models


def get_token_for_user(
    username: str,
) -> typing.Union[rest_framework_simplejwt.tokens.AccessToken, str]:
    """получаем access_token для пользователя username"""
    user_obj = users.models.User.objects.filter(
        username__exact=username
    ).first()
    if user_obj:
        token = rest_framework_simplejwt.tokens.RefreshToken.for_user(user_obj)
        return token.access_token
    return 'fake_token'


def get_test_client(username: str) -> rest_framework.test.APIClient:
    """получаем тестовый клиент пользователя по username"""
    client = rest_framework.test.APIClient()
    client.credentials(
        HTTP_AUTHORIZATION=f'Bearer {get_token_for_user(username)}'
    )
    return client
