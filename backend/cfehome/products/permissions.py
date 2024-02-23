import rest_framework.permissions
import rest_framework.views

import django.http

import products.models


class RetrieveUpdateDestroyProductPermission(
    rest_framework.permissions.BasePermission
):
    """
    проверяем возможность пользователя смотреть, редактировать и изменять товар
    """

    methods = {
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete',
        'GET': 'view',
    }

    def has_object_permission(
        self,
        request: django.http.HttpRequest,
        view: rest_framework.views.APIView,
        obj: products.models.Product,
    ):
        if (
            request.method in rest_framework.permissions.SAFE_METHODS
            and obj.is_public
        ):
            return True
        user = request.user
        if obj.user and user.pk == obj.user.pk:
            return True
        if user.is_staff and user.has_perm(
            f'products.{self.methods[request.method]}_product'
        ):
            return True
        return False
