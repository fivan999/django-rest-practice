import rest_framework.permissions
import rest_framework.serializers
import rest_framework.viewsets

import products.models
import products.permissions
import products.serializers


class ProductViewSet(rest_framework.viewsets.ModelViewSet):
    """вьюсет для модели Product"""

    queryset = products.models.Product.objects.all()

    def get_serializer_class(self) -> rest_framework.serializers.Serializer:
        """получаем serializer для запроса"""
        if self.action == 'list':
            return products.serializers.ProductListSerializer
        return products.serializers.ProductDetailSerializer

    def get_permissions(self) -> list:
        """
        permissions в зависисмости от action
        """
        if self.action in ('list', 'create'):
            permission_classes = [
                rest_framework.permissions.IsAuthenticatedOrReadOnly
            ]
        else:
            permission_classes = [
                products.permissions.RetrieveUpdateDestroyProductPermission
            ]
        return [permission() for permission in permission_classes]

    def perform_create(
        self, serializer: rest_framework.serializers.Serializer
    ) -> None:
        """
        установить значение description в title,
        если description пустой
        и привязать пользователя
        """
        description = serializer.validated_data.get('description')
        if not description:
            serializer.validated_data[
                'description'
            ] = serializer.validated_data.get('title')
        serializer.save(user=self.request.user)

    def perform_update(
        self, serializer: rest_framework.serializers.Serializer
    ) -> None:
        """установить значение description в title, если description пустой"""
        if not serializer.validated_data.get('description'):
            serializer.validated_data[
                'description'
            ] = serializer.validated_data.get('title')
        serializer.save()
