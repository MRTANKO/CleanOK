"""Представления приложения services."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import BasePermission, DjangoModelPermissions

from .models import Service, Category, Request
from .serializers import ServiceSerializer, CategorysSerializer, \
    CreateRequestSerializer, RequestsSerializer


class Services(generics.ListAPIView):
    """API услуг."""

    queryset = Service.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = ServiceSerializer


class CategoryAPI(generics.ListAPIView):
    """API категорий."""

    queryset = Category.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CategorysSerializer


class PostOnly(BasePermission):
    """Класс для настройки доступа."""

    def has_permission(self, request, view):
        """Обрабатывает разрешение.

        Возвращает 'True', если разрешение предоставлено.
        Возвращает 'False' в противном случае.
        """
        return request.method == 'POST'


class RequestAPI(generics.ListCreateAPIView):
    """API запросов."""

    queryset = Request.objects.all()
    serializer_class = CreateRequestSerializer
    pagination_class = PageNumberPagination
    permission_classes = (DjangoModelPermissions | PostOnly,)

    def get(self, request, *args, **kwargs):
        """Обрабатывает get запрос."""
        groups = Request.objects.all()
        serializer = RequestsSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
