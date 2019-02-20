from rest_framework import serializers
from .models import Promo


class PromoSerializer(serializers.ModelSerializer):
    """Сериализация рекомендации"""
    class Meta:
        model = Promo
        fields = ('id',  'date', 'title', 'preview')
