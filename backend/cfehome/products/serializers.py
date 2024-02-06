import rest_framework.serializers

import products.models


class ProductSerializer(rest_framework.serializers.ModelSerializer):
    """сериализация модели Product"""

    class Meta:
        model = products.models.Product
        fields = [
            'title',
            'description',
            'price',
        ]
