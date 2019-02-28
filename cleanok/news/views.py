"""Представления приложения news."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import News
from .serializers import NewSerializer


class News(generics.ListAPIView):
    """API новостей."""

    queryset = News.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = NewSerializer
