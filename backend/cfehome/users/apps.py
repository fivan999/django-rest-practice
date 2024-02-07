import django.apps


class UsersConfig(django.apps.AppConfig):
    """базовый класс приложения Users"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'пользователи'
