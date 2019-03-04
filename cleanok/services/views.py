"""Представления приложения services."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from .models import Service, Category, Request
from .serializers import ServiceSerializer, CategoriesSerializer, \
    CreateRequestSerializer, RequestsSerializer
from base.postonly import PostOnly


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
    #serializer_class = CreateRequestSerializer
    pagination_class = PageNumberPagination
    permission_classes = (DjangoModelPermissions | PostOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateRequestSerializer
        return RequestsSerializer
