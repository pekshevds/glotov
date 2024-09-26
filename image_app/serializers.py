from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    url = serializers.ImageField(use_url=True, source="image")
