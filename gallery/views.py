from .models import Group
from .serializers import GroupSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Groups(generics.ListAPIView):
    """Фотоальбомы API"""
    queryset = Group.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
