"""Сериализатор приложения certificate."""
from rest_framework import serializers

from .models import Certificate


class CertSerializer(serializers.ModelSerializer):
    """Сериализация сертификата."""

    class Meta:
        """Настройки сериализатора."""

        model = Certificate
        fields = ('url', 'title', 'subt',)
