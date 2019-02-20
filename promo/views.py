from .models import Promo
from .serializers import PromoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Promos(generics.ListAPIView):
    """Рекомендации API"""
    queryset = Promo.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        promos = Promo.objects.all()
        serializer = PromoSerializer(promos, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
