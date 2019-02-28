"""Администрирование приложения news."""
from django.contrib import admin

from .models import News


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    """Редактирвание новости."""

    list_display = ('title', 'date', 'preview')
