import django_elasticsearch_dsl
import django_elasticsearch_dsl.fields
import django_elasticsearch_dsl.registries
import users.models

import products.models


@django_elasticsearch_dsl.registries.registry.register_document
class ProductDocument(django_elasticsearch_dsl.Document):
    """документ для поиска elastic по модели Product"""

    user = django_elasticsearch_dsl.fields.ObjectField(
        properties={
            'username': django_elasticsearch_dsl.fields.TextField(),
        }
    )

    class Index:
        name = 'products'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = products.models.Product
        fields = [
            'title',
            'description',
        ]
        related_models = [users.models.User]

    def get_queryset(self):
        """добавляем пользователя к товарам"""
        return super().get_queryset().select_related('user')
