import django.apps


class ApiConfig(django.apps.AppConfig):
    """баззовый класс прилложения api"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    verbose_name = 'апи'
