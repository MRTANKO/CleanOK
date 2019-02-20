from .models import Service, Category, Request, Message
from .serializers import ServiceSerializer, CategorysSerializer, RequestSerializer, RequestsSerializer, \
    MessageSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Services(generics.ListAPIView):
    """Услуги API"""
    queryset = Service.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        groups = Service.objects.all()
        serializer = ServiceSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class CategoryAPI(generics.ListAPIView):
    """Категории API"""
    queryset = Category.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        groups = Category.objects.all()
        serializer = CategorysSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class RequestAPI(generics.ListCreateAPIView):
    """Запросы API"""
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def get(self, request, *args, **kwargs):
        groups = Request.objects.all()
        serializer = RequestsSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageAPI(generics.ListCreateAPIView):
    """Сообщения API"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        groups = Message.objects.all()
        serializer = MessageSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
