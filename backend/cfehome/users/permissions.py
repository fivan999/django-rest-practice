import rest_framework.permissions

import django.http

import users.models


class IsAdminOrIsSelf(rest_framework.permissions.BasePermission):
    """
    проверяем возможность пользователя смотреть,
    редактировать и изменять пользователя
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
        obj: users.models.User,
    ):
        user = request.user
        if not user:
            return False
        if (
            user.pk == obj.pk
            or user.is_staff
            and user.has_perm(f'users.{self.methods[request.method]}_user')
        ):
            return True
        return False
