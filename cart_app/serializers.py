from rest_framework import serializers
from catalog_app.serializers import GoodSerializer


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    is_active = serializers.BooleanField()


class CartSerializer(serializers.Serializer):
    good = GoodSerializer()
    qnt = serializers.DecimalField(max_digits=15, decimal_places=3)


class SimpleCartSerializer(serializers.Serializer):
    good_id = serializers.UUIDField()
    qnt = serializers.DecimalField(max_digits=15, decimal_places=3)
