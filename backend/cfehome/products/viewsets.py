import rest_framework.permissions
import rest_framework.serializers
import rest_framework.viewsets

import django.db.models
import django.http

import products.models
import products.permissions
import products.serializers
import search.mixins
import search.services


class ProductViewSet(
    search.mixins.ListSearchMixin, rest_framework.viewsets.ModelViewSet
):
    """вьюсет для модели Product"""

    queryset = products.models.Product.objects.all()
    availabe_search_params = {'user': str, 'is_public': lambda val: val == '1'}
    index_name = 'product_index'

    def get_default_queryset(self) -> django.db.models.QuerySet:
        """получаем базовый queryset для поиска по нему"""
        user_pk = None
        if self.request.user.is_authenticated:
            user_pk = self.request.user.pk
        user_based_queryset = (
            products.models.Product.objects.search_by_user(user_pk)
        ).select_related('user')
        return user_based_queryset

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
