import django.apps


class ApiConfig(django.apps.AppConfig):
    """Базовый класс приложения api"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'апи'
