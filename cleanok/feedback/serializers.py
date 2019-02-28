"""Сериализатор приложения feedback."""
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """Сериализатор для создания и вывода сообщения."""

    class Meta:
        """Настройки сериализатора."""

        model = Message
        fields = ('id', 'first_name', 'last_name', 'message')

    def create(self, validated_data):
        """Создание сообщения."""
        return Message.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            message=validated_data['message']
        )
