import django.contrib.auth.models
import django.db.models
from django.utils.translation import gettext_lazy as _

import users.managers


class User(django.contrib.auth.models.AbstractUser):
    """кастомный пользователь"""

    objects = users.managers.UserManager()

    email = django.db.models.EmailField(
        verbose_name=_('email address'), unique=True
    )

    class Meta(django.contrib.auth.models.AbstractUser.Meta):
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
