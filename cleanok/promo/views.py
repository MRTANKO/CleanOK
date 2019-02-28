"""Представления приложения promo."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Promo
from .serializers import PromoSerializer


class Promos(generics.ListAPIView):
    """API акций."""

    queryset = Promo.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = PromoSerializer
