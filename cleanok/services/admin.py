"""Администрирование приложения vacancy."""
from django.contrib import admin

from .models import Service, Item, Category, Request


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Редактирование услуг."""

    list_display = ['category', 'name', 'desc']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Редактирование пунктов работы."""

    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Редактирование категорий."""

    list_display = ['name']


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    """Редактирование запросов."""

    list_display = ['name', 'phone', 'service', 'comment']
