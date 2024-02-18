import rest_framework.reverse
import rest_framework.serializers

import products.models
import users.serializers


class ProductListSerializer(rest_framework.serializers.ModelSerializer):
    """сериализация модели Product"""

    url = rest_framework.serializers.HyperlinkedIdentityField(
        view_name='products:product-detail'
    )
    user = users.serializers.UserPublicSerializer(read_only=True)

    class Meta:
        model = products.models.Product
        fields = ['pk', 'url', 'title', 'price', 'description', 'user']


class ProductDetailSerializer(rest_framework.serializers.ModelSerializer):
    """сериализация модели Product"""

    user = users.serializers.UserPublicSerializer(read_only=True)

    class Meta:
        model = products.models.Product
        fields = [
            'pk',
            'title',
            'description',
            'price',
            'user',
        ]

    def create(self, validated_data: dict) -> products.models.Product:
        """
        установить значение description в title, если description пустой
        """
        description = validated_data.get('description')
        if not description:
            validated_data['description'] = validated_data.get('title')
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)

    def update(
        self, instance: products.models.Product, validated_data: dict
    ) -> products.models.Product:
        """установить значение description в title, если description пустой"""
        description = validated_data.get('description')
        if not description:
            validated_data['description'] = validated_data.get('title')
        return super().update(instance, validated_data)

    def validate_title(self, title: str) -> str:
        """существует ли у пользователя товар с таким названием"""
        user_pk = self.context.get('request').user.pk
        queryset = products.models.Product.objects.filter(
            user__pk=user_pk, title__iexact=title
        )
        if queryset.exists():
            raise rest_framework.serializers.ValidationError(
                f'У вас уже есть товар с названием: {title}'
            )
        return title
