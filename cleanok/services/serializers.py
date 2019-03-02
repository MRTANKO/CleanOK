"""Сериализатор приложения services."""
from rest_framework import serializers

from .models import Service, Item, Category, Request


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий для услуги."""

    class Meta:
        """Настройки сериализатора."""

        model = Category
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    """Сериализация пунктов работ."""

    class Meta:
        """Настройки сериализатора."""

        model = Item
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализация услуг."""

    items = ItemSerializer(many=True)
    category = CategorySerializer()
    price = serializers.SerializerMethodField('text_price')

    @staticmethod
    def text_price(obj):
        """Форматирование цены услуги."""
        return 'От {} рублей'.format(obj.price)

    class Meta:
        """Настройки сериализатора."""

        model = Service
        fields = (
            'id', 'category', 'name', 'desc', 'items', 'price', 'note', 'warn')


class SerevicesSerializer(serializers.ModelSerializer):
    """Сериализация услуг принадлежащих категории."""

    class Meta:
        """Настройки сериализатора."""

        model = Service
        fields = ('id', 'name')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализация категорий с выводом всех услуг этой категориии."""

    items = serializers.SerializerMethodField('_get_services')

    @staticmethod
    def _get_services(obj):
        """Получение всех детей модели Категории."""
        serializer = SerevicesSerializer(
            Service.objects.filter(category=obj), many=True)
        return serializer.data

    class Meta:
        """Настройки сериализатора."""

        model = Category
        fields = ('id', 'name', 'items')


class CreateRequestSerializer(serializers.ModelSerializer):
    """Сериализатор для создания запроса."""

    def create(self, validated_data):
        """Создание запроса."""
        return Request.objects.create(
            name=validated_data['name'],
            phone=validated_data['phone'],
            service=validated_data['service'],
            comment=validated_data['comment']
        )

    class Meta:
        """Настройки сериализатора."""

        model = Request
        fields = ('id', 'name', 'phone', 'service', 'comment')


class RequestsSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода запроса."""

    service = SerevicesSerializer()

    class Meta:
        """Настройки сериализатора."""

        model = Request
        fields = ('id', 'name', 'phone', 'service', 'comment')
