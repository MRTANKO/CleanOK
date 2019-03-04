"""Представления приложения services."""
from base.postonly import PostOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from .models import Service, Category, Request
from .serializers import ServiceSerializer, CategoriesSerializer, \
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
    serializer_class = CategoriesSerializer


class RequestAPI(generics.ListCreateAPIView):
    """API запросов."""

    queryset = Request.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (DjangoModelPermissions | PostOnly,)

    def get_serializer_class(self):
        """Выбор сериализатора."""
        if self.request.method == 'POST':
            return CreateRequestSerializer
        return RequestsSerializer
