import typing

import django.contrib.auth.models
import django.core.exceptions
import django.db.models


class UserManager(django.contrib.auth.models.UserManager):
    """менеджер модели User"""

    def get_user_by_username_or_email(
        self, username: str
    ) -> typing.Optional[django.contrib.auth.models.AbstractUser]:
        """получаем объект пользователя по имени username или почте email"""
        return (
            self.get_queryset()
            .filter(
                django.db.models.Q(username=username)
                | django.db.models.Q(email=self.normalize_email(username))
            )
            .first()
        )

    @classmethod
    def normalize_email(cls, email: str) -> str:
        """костомная нормализация email"""
        if not email or '@' not in email:
            return ''
        username, domain = email.lower().strip().split('@')

        if '+' in username:
            username = username[: username.find('+')]

        if domain in ('ya.ru', 'yandex.ru'):
            username = username.replace('.', '-')
            domain = 'yandex.ru'
        elif domain == 'gmail.com':
            username = username.replace('.', '')

        return f'{username}@{domain}'

    def create_superuser(
        self, username: str, email: str, password: str, **extra_fields
    ) -> typing.Any:
        """переопределяем создание суперпользователя"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        email = self.normalize_email(email)
        if self.get_queryset().filter(email=email).exists():
            raise django.core.exceptions.ValidationError(
                'Пользователь уже существует'
            )
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
