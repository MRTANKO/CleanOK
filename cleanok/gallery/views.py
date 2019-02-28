"""Представления приложения gallery."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Group
from .serializers import GroupSerializer


class Groups(generics.ListAPIView):
    """API фотоальбомов."""

    queryset = Group.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = GroupSerializer
