import http

import rest_framework.decorators
import rest_framework.mixins
import rest_framework.response
import rest_framework.views
import rest_framework.viewsets

import django.contrib.auth.tokens
import django.http
import django.utils.encoding
import django.utils.http

import users.models
import users.permissions
import users.serializers


class UserViewSet(
    rest_framework.mixins.CreateModelMixin,
    rest_framework.viewsets.GenericViewSet,
):
    """viewset для пользователя"""

    queryset = users.models.User.objects.all()
    serializer_class = users.serializers.UserCreateSerializer

    def get_permissions(self) -> list:
        """
        permissions в зависисмости от action
        """
        permission_classes = []
        if self.action == 'change_password':
            permission_classes = [users.permissions.IsAdminOrIsSelf]
        return [permission() for permission in permission_classes]

    @rest_framework.decorators.action(
        detail=False,
        methods=['get'],
    )
    def activate_user(
        self, request: django.http.HttpRequest, uidb64: str, token: str
    ) -> django.http.HttpResponse:
        """активация аккаунта пользователя"""
        account_activated = False
        try:
            user = users.models.User.objects.get(
                pk=django.utils.encoding.force_str(
                    django.utils.http.urlsafe_base64_decode(uidb64)
                )
            )
        except users.models.User.DoesNotExist:
            user = None
        if (
            user
            and django.contrib.auth.tokens.default_token_generator.check_token(
                user, token
            )
        ):
            user.is_active = True
            user.save()
            account_activated = True
        return rest_framework.response.Response(
            {'account_activated': account_activated},
            status=(
                http.HTTPStatus.OK
                if account_activated
                else http.HTTPStatus.NOT_FOUND
            ),
        )

    @rest_framework.decorators.action(
        detail=True,
        methods=['put', 'patch'],
    )
    def change_password(
        self, request: django.http.HttpRequest, pk: int
    ) -> django.http.HttpResponse:
        """изменение пароля пользователя"""
        user = self.get_object()
        serializer = users.serializers.UserPasswordSerializer(
            data=request.data, instance=user
        )
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return rest_framework.response.Response(
                {'status': 'password set'}, status=http.HTTPStatus.NO_CONTENT
            )
        else:
            return rest_framework.response.Response(
                serializer.errors, status=http.HTTPStatus.BAD_REQUEST
            )
