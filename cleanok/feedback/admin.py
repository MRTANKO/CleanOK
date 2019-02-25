"""Администрирование приложения news."""
from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Редактирвание сообщений."""

    list_display = ('first_name', 'last_name', 'message')
