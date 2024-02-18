import rest_framework.permissions
import rest_framework.serializers
import rest_framework.viewsets

import django.db.models
import django.http

import products.models
import products.permissions
import products.search_service
import products.serializers


class ProductViewSet(rest_framework.viewsets.ModelViewSet):
    """вьюсет для модели Product"""

    queryset = products.models.Product.objects.all()

    def get_queryset(self) -> django.db.models.QuerySet:
        """
        получаем queryset в зависимости от
        поискового запроса и пользователя
        """
        if self.action == 'list':
            user_pk = None
            if self.request.user.is_authenticated:
                user_pk = self.request.user.pk
            user_based_queryset = (
                products.models.Product.objects.search_by_user(user_pk)
            )

            query = self.request.GET.get('query', '')
            if not query:
                return user_based_queryset

            return user_based_queryset.filter(
                pk__in=products.search_service.perform_search(
                    query, 'product_index'
                )
            )
        return self.__class__.queryset

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

    # def list(
    #     self, request: django.http.HttpRequest, *args, **kwargs
    # ) -> django.http.HttpResponse:
    #     """список элементов"""
    #     return super().list(request, *args, **kwargs)
