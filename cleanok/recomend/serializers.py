"""Сериализатор приложения recomend."""
from rest_framework import serializers

from .models import Recomend


class RecSerializer(serializers.ModelSerializer):
    """Сериализация рекомендации."""

    year = serializers.SerializerMethodField('text_year')

    @staticmethod
    def text_year(obj):
        """Форматирование года."""
        return str(obj.year) + ' год'

    class Meta:
        """Настройки сериализатора."""

        model = Recomend
        fields = ('url', 'title', 'year',)
