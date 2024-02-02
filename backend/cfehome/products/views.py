import products.models
import products.serializers
import rest_framework.generics


class ProductListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """создание товара"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductSerializer


class ProductDetailAPIView(rest_framework.generics.RetrieveAPIView):
    """просмотр одного товара"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductSerializer
