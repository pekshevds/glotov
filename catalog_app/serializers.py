from rest_framework import serializers
from image_app.serializers import ImageSerializer
from catalog_app.models import Good, Manufacturer, Category


class ManufacturerSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        manufacturer, _ = Manufacturer.objects.get_or_create(
            id=validated_data.get("id")
        )
        manufacturer.name = validated_data.get("name", manufacturer.name)
        manufacturer.save()
        return manufacturer


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)

    def create(self, validated_data):
        category, _ = Category.objects.get_or_create(id=validated_data.get("id"))
        category.name = validated_data.get("name", category.name)
        category.save()
        return category


class GoodsImageSerializer(serializers.Serializer):
    image = ImageSerializer(required=False, allow_null=True)


class GoodSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=150)
    art = serializers.CharField(max_length=50, required=False, allow_blank=True)
    code = serializers.CharField(max_length=11, required=False, allow_blank=True)
    balance = serializers.DecimalField(max_digits=15, decimal_places=3, required=False)
    price = serializers.DecimalField(max_digits=15, decimal_places=2, required=False)
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    category = CategorySerializer(required=False, allow_null=True)
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
    manufacturer_id = serializers.UUIDField(required=False, allow_null=True)
    category_id = serializers.UUIDField(required=False, allow_null=True)
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
    manufacturer = ManufacturerSerializer(required=False, allow_null=True)
    category = CategorySerializer(required=False, allow_null=True)

    def create(self, validated_data):
        good, _ = Good.objects.get_or_create(id=validated_data.get("id"))
        good.name = validated_data.get("name", good.name)
        good.art = validated_data.get("art", good.art)
        good.code = validated_data.get("code", good.code)
        good.balance = validated_data.get("balance", good.balance)
        good.price = validated_data.get("price", good.price)
        good.description = validated_data.get("description", good.description)
        good.comment = validated_data.get("comment", good.comment)

        manufacturer_data = validated_data.get("manufacturer")
        if manufacturer_data:
            manufacturer, _ = Manufacturer.objects.get_or_create(
                id=manufacturer_data.get("id")
            )
            manufacturer.name = manufacturer_data.get("name", manufacturer.name)
            manufacturer.save()
            good.manufacturer = manufacturer

        category_data = validated_data.get("category")
        if category_data:
            category, _ = Category.objects.get_or_create(id=category_data.get("id"))
            category.name = category_data.get("name", category.name)
            category.save()
            good.category = category
        good.save()
        return good
