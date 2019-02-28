"""Представления приложения recomend."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Recomend
from .serializers import RecSerializer


class Recomends(generics.ListAPIView):
    """API рекомендаций."""

    queryset = Recomend.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = RecSerializer
