import rest_framework.reverse
import rest_framework.serializers

import products.models


class ProductListSerializer(rest_framework.serializers.ModelSerializer):
    """сериализация модели Product"""

    url = rest_framework.serializers.HyperlinkedIdentityField(
        view_name='products:product-detail'
    )

    class Meta:
        model = products.models.Product
        fields = [
            'pk',
            'url',
            'title',
            'price',
        ]


class ProductDetailSerializer(rest_framework.serializers.ModelSerializer):
    """сериализация модели Product"""

    class Meta:
        model = products.models.Product
        fields = [
            'pk',
            'title',
            'description',
            'price',
            'user',
        ]
        read_only_fields = ['user']
