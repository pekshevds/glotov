from rest_framework import serializers
from image_app.serializers import ImageSerializer
from catalog_app.models import Good


class GoodsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    manufacturer = serializers.CharField(
        max_length=150, required=False, allow_blank=True
    )
    description = serializers.CharField(
        max_length=1024, required=False, allow_null=True
    )
    comment = serializers.CharField(required=False, allow_null=True)
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )


class SimpleGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    description = serializers.CharField(
        max_length=1024, required=False, allow_null=True
    )
    comment = serializers.CharField(required=False, allow_null=True)
    manufacturer = serializers.CharField(
        max_length=150, required=False, allow_blank=True
    )
    preview = ImageSerializer(
        required=False, allow_null=True, source="image", read_only=True
    )
    images = GoodsImageSerializer(
        required=False, allow_null=True, many=True, read_only=True
    )


class UploadGoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    description = serializers.CharField(
        max_length=1024, required=False, allow_null=True, allow_blank=True
    )
    comment = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    manufacturer = serializers.CharField(
        max_length=150, required=False, allow_blank=True
    )

    def create(self, validated_data):
        good, _ = Good.objects.get_or_create(id=validated_data.get("id"))
        good.name = validated_data.get("name", good.name)
        good.art = validated_data.get("art", good.art)
        good.code = validated_data.get("code", good.code)
        good.balance = validated_data.get("balance", good.balance)
        good.price = validated_data.get("price", good.price)
        good.description = validated_data.get("description", good.description)
        good.manufacturer = validated_data.get("manufacturer", good.manufacturer)
        good.comment = validated_data.get("comment", good.comment)

        good.save()
        return good
