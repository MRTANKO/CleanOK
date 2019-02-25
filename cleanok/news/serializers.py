"""Сериализатор приложения news."""
from rest_framework import serializers

from .models import News


class NewSerializer(serializers.ModelSerializer):
    """Сериализация новости."""

    class Meta:
        """Настройки сериализатора."""

        model = News
        fields = ('id', 'date', 'title', 'preview', 'text', 'related')
