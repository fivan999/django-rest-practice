import django.contrib

import products.models


@django.contrib.admin.register(products.models.Product)
class ProductAdmin(django.contrib.admin.ModelAdmin):
    """отображение модели Product в админке"""

    list_display = ('id', 'title')
    list_display_links = ('id',)
    list_editable = ('title',)
