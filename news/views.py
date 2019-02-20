from .models import New
from .serializers import NewSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class News(generics.ListAPIView):
    """Новости API"""
    queryset = New.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        news = New.objects.all()
        serializer = NewSerializer(news, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
