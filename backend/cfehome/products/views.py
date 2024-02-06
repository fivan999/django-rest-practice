import products.models
import products.serializers
import rest_framework.generics
import rest_framework.serializers


class ProductListCreateAPIView(rest_framework.generics.ListCreateAPIView):
    """создание товара и список товаров"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductSerializer

    def perform_create(
        self, serializer: rest_framework.serializers.Serializer
    ) -> None:
        """установить значение description в title, если description пустой"""
        description = serializer.validated_data.get('description')
        if not description:
            serializer.validated_data[
                'description'
            ] = serializer.validated_data.get('title')
        serializer.save()


class ProductDetailAPIView(rest_framework.generics.RetrieveAPIView):
    """просмотр одного товара"""

    queryset = products.models.Product.objects.all()
    serializer_class = products.serializers.ProductSerializer
