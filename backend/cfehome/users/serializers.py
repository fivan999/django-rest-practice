import rest_framework.serializers

import django.conf
import django.contrib.auth.tokens
import django.contrib.sites.shortcuts

import users.models
import users.tasks


class UserPublicSerializer(rest_framework.serializers.Serializer):
    """serializer для данных пользователя"""

    pk = rest_framework.serializers.IntegerField(read_only=True)
    username = rest_framework.serializers.CharField(read_only=True)


class UserCreateSerializer(rest_framework.serializers.ModelSerializer):
    """serializer для создания пользователя"""

    password = rest_framework.serializers.CharField(write_only=True)
    is_active = rest_framework.serializers.BooleanField(read_only=True)

    class Meta:
        model = users.models.User
        fields = [
            'pk',
            'username',
            'password',
            'email',
            'is_active',
        ]

    def create(self, validated_data: dict) -> users.models.User:
        """
        создание объекта User
        и отправка ему письма с подтвержением если он не активный
        """
        user_obj = users.models.User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_active=django.conf.settings.USER_IS_ACTIVE,
        )
        if not django.conf.settings.USER_IS_ACTIVE:
            token_generator = (
                django.contrib.auth.tokens.default_token_generator
            )
            request = self.context['request']
            users.tasks.send_email_with_token(
                user_id=user_obj.pk,
                template_name='users/emails/activate_user.html',
                subject='Активация аккаунта',
                where_to='auth:activate_user',
                protocol='https' if request.is_secure() else 'http',
                domain=django.contrib.sites.shortcuts.get_current_site(
                    request
                ).domain,
                token=token_generator.make_token(user_obj),
            )
        return user_obj


class UserPasswordSerializer(rest_framework.serializers.ModelSerializer):
    """serializer для пароля пользователя"""

    old_password = rest_framework.serializers.CharField(write_only=True)

    class Meta:
        model = users.models.User
        fields = ['old_password', 'password']

    def validate_old_password(self, value: str) -> str:
        """проверяем, правильный ли старый палоль"""
        if not self.instance.check_password(value):
            raise rest_framework.serializers.ValidationError(
                'old password is wrong'
            )
        return value
