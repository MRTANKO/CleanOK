from rest_framework import serializers
from .models import Group, Image


class ImgSerializer(serializers.ModelSerializer):
    """Сериализация фотографии"""

    class Meta:
        model = Image
        fields = ('img',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализация альбома"""
    items = ImgSerializer(many=True)

    class Meta:
        model = Group
        fields = ('title', 'cover', 'items')
