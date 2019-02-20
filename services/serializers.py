from rest_framework import serializers
from .models import Service, Item, Category, Request, Message


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий для услуги"""

    class Meta:
        model = Category
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    """Сериализация пунктов работ"""

    class Meta:
        model = Item
        fields = ('id', 'name')


class ServiceSerializer(serializers.ModelSerializer):
    """Сериализация услуг"""
    items = ItemSerializer(many=True)
    category = CategorySerializer()
    price = serializers.SerializerMethodField('text_price')

    @staticmethod
    def text_price(obj):
        return 'От {} рублей'.format(obj.price)

    class Meta:
        model = Service
        fields = ('id', 'category', 'name', 'desc', 'items', 'price', 'note', 'warn')


class SerevicesSerializer(serializers.ModelSerializer):
    """Сериализация услуг принадлежащих категории категории"""
    class Meta:
        model = Service
        fields = ('id', 'name')


class CategorysSerializer(serializers.ModelSerializer):
    """Сериализация категорий с выводом всех услуг этой категориии"""
    items = serializers.SerializerMethodField('_get_servicec')

    @staticmethod
    def _get_servicec(obj):
        """Получение всех детей модели Категории"""
        serializer = SerevicesSerializer(Service.objects.filter(category=obj), many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'items')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('id', 'name', 'phone', 'service', 'comment')

    def create(self, validated_data):
        return Request.objects.create(name=validated_data['name'], phone=validated_data['phone'],
                                      service=validated_data['service'], comment=validated_data['comment'])


class RequestsSerializer(serializers.ModelSerializer):
    service = SerevicesSerializer()

    class Meta:
        model = Request
        fields = ('id', 'name', 'phone', 'service', 'comment')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'first_name', 'last_name', 'message')

    def create(self, validated_data):
        return Message.objects.create(first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                                      message=validated_data['message'])
