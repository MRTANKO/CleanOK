"""Администрирование приложения recomend."""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Recomend


@admin.register(Recomend)
class RecomendAdmin(admin.ModelAdmin):
    """Редактирование рекомендаций."""

    def recomend_img(self, obj):
        """Получение фотографии рекомендации."""
        if obj.url:
            return mark_safe('<img src="%s" width="300"/>' % obj.url.url)
        else:
            return 'No Image Found'

    recomend_img.allow_tags = True
    recomend_img.short_description = 'Фотография рекомендации'

    list_display = ('title', 'recomend_img', 'year')
