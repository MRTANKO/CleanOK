from rest_framework import serializers
from .models import New


class NewSerializer(serializers.ModelSerializer):
    """Сериализация новости"""

    class Meta:
        model = New
        fields = ('id', 'date', 'title', 'preview', 'text', 'related')
