from rest_framework import serializers
from .models import Sertificate


class SertSerializer(serializers.ModelSerializer):
    """Сериализация сертификата"""

    class Meta:
        model = Sertificate
        fields = ('usl', 'title', 'subt',)
