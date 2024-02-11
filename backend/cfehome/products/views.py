import rest_framework.authentication
import rest_framework.generics
import rest_framework.permissions
import rest_framework.serializers

import products.models
import products.permissions
import products.serializers


class ProductListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """создание товара и список товаров"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductListSerializer

    def perform_create(
        self, serializer: rest_framework.serializers.Serializer
    ) -> None:
        """установить значение description в title, если description пустой"""
        description = serializer.validated_data.get('description')
        if not description:
            serializer.validated_data[
                'description'
            ] = serializer.validated_data.get('title')
        serializer.save(user=self.request.user)


class ProductDetailAPIView(
    rest_framework.generics.RetrieveUpdateDestroyAPIView
):
    """просмотр, обновление и удаление одного товара"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductDetailSerializer
    permission_classes = [
        products.permissions.RetrieveUpdateDestroyProductPermission
    ]

    def perform_update(
        self, serializer: rest_framework.serializers.Serializer
    ) -> None:
        """установить значение description в title, если description пустой"""
        if not serializer.validated_data.get('description'):
            serializer.validated_data[
                'description'
            ] = serializer.validated_data.get('title')
        serializer.save()
