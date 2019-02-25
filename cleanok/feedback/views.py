"""Представления приложения feedback."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import BasePermission, DjangoModelPermissions

from .models import Message
from .serializers import MessageSerializer


class PostOnly(BasePermission):
    """Класс для настройки доступа."""

    def has_permission(self, request, view):
        """Обрабатывает разрешение.

        Возвращает 'True', если разрешение предоставлено.
        Возвращает 'False' в противном случае.
        """
        return request.method == 'POST'


class MessageAPI(generics.ListCreateAPIView):
    """API сообщений."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
    permission_classes = (DjangoModelPermissions | PostOnly,)
