import products.models
import products.serializers
import rest_framework.decorators
import rest_framework.response

import django.forms
import django.http


@rest_framework.decorators.api_view(http_method_names=['GET'])
def home(request: django.http.HttpRequest) -> django.http.JsonResponse:
    """список всех товаров"""
    instances = products.models.Product.objects.all()
    result_data = products.serializers.ProductSerializer(
        instances, many=True
    ).data
    return rest_framework.response.Response(result_data)
