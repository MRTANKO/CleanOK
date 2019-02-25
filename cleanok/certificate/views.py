"""Представления приложения certificate."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Certificate
from .serializers import CertSerializer


class Certificates(generics.ListAPIView):
    """API сертификатов."""

    queryset = Certificate.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = CertSerializer
