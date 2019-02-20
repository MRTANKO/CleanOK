from django.contrib import admin
from .models import Service, Item, Category, Request, Message


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'desc']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Request)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'comment']


@admin.register(Message)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'message']
