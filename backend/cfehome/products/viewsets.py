import rest_framework.permissions
import rest_framework.serializers
import rest_framework.viewsets

import django.db.models

import products.models
import products.permissions
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
            return products.models.Product.objects.search_by_query_and_user(
                query=self.request.GET.get('query', ''), user_pk=user_pk
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
