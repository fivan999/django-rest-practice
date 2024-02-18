import django.apps


class SearchConfig(django.apps.AppConfig):
    """базовый класс приложения Search"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'
    verbose_name = 'поиск'
