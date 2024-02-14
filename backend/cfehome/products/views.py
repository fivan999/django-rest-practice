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


class ProductDetailAPIView(
    rest_framework.generics.RetrieveUpdateDestroyAPIView
):
    """просмотр, обновление и удаление одного товара"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductDetailSerializer
    permission_classes = [
        products.permissions.RetrieveUpdateDestroyProductPermission
    ]
