import django.apps


class ProductsConfig(django.apps.AppConfig):
    """базовый класс приложения products"""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    verbose_name = 'товары'
