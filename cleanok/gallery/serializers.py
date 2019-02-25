"""Сериализатор приложения gallery."""
from rest_framework import serializers

from .models import Group, Image


class ImgSerializer(serializers.ModelSerializer):
    """Сериализация фотографии."""

    class Meta:
        """Настройки сериализатора."""

        model = Image
        fields = ('img',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализация альбома."""

    items = ImgSerializer(many=True)

    class Meta:
        """Настройки сериализатора."""

        model = Group
        fields = ('title', 'cover', 'items')
