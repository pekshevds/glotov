from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    token = serializers.UUIDField()


class DataSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField(allow_blank=True, required=False)
    phone = serializers.CharField(max_length=150, allow_blank=True, required=False)


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()
