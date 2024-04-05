from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers



class UserCreateSerializer(BaseUserCreateSerializer):
    username = serializers.CharField(required=True, allow_blank=False, min_length=3)
    first_name = serializers.CharField(required=True, allow_blank=False, min_length=3)
    last_name = serializers.CharField(required=True, allow_blank=False, min_length=3)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']