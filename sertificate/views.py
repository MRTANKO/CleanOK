from .models import Sertificate
from .serializers import SertSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Sertificates(generics.ListAPIView):
    """Сертификаты API"""
    queryset = Sertificate.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        sertificates = Sertificate.objects.all()
        serializer = SertSerializer(sertificates, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
