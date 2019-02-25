"""Администрирование приложения promo."""
from django.contrib import admin

from .models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    """Редактирование акций."""

    list_display = ('title', 'preview', 'date')
