"""Представления приложения feedback."""
from base.postonly import PostOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from .models import Message
from .serializers import MessageSerializer


class MessageAPI(generics.ListCreateAPIView):
    """API сообщений."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = PageNumberPagination
    permission_classes = (DjangoModelPermissions | PostOnly,)
