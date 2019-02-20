from .models import Recomend
from .serializers import RecSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Recomends(generics.ListAPIView):
    """Рекомендации API"""
    queryset = Recomend.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        recomends = Recomend.objects.all()
        serializer = RecSerializer(recomends, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
