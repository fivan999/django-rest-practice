import django.contrib.auth.models

import users.managers


class User(django.contrib.auth.models.AbstractUser):
    """кастомный пользователь"""

    objects = users.managers.UserManager()

    class Meta(django.contrib.auth.models.AbstractUser.Meta):
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
