import django.db.models


class Product(django.db.models.Model):
    """модель товара"""

    title = django.db.models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Введите название товара'
    )

    description = django.db.models.TextField(
        max_length=1000,
        verbose_name='описание',
        help_text='Введите описание товара',
        blank=True,
        null=True
    )

    price = django.db.models.DecimalField(
        verbose_name='цена',
        help_text='Введите цену товара',
        decimal_places=2,
        max_digits=15
    )

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self) -> str:
        """строковое представление товара"""
        return self.title[:15]
