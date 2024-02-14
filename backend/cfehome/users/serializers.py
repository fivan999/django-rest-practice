import rest_framework.serializers


class UserPublicSerializer(rest_framework.serializers.Serializer):
    """serializer для данных пользователя"""

    pk = rest_framework.serializers.IntegerField(read_only=True)
    username = rest_framework.serializers.CharField(read_only=True)
