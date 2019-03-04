"""Настройка доступа к API."""
from rest_framework.permissions import BasePermission


class PostOnly(BasePermission):
    """Класс для настройки доступа."""

    def has_permission(self, request, view):
        """Обрабатывает разрешение.

        Возвращает 'True', если разрешение предоставлено.
        Возвращает 'False' в противном случае.
        """
        return request.method == 'POST'
