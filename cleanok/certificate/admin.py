"""Администрирование приложения certificate."""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Редактирование сертификатов."""

    def cetrificate_img(self, obj):
        """Получение фотографии сертификата."""
        if obj.url:
            return mark_safe('<img src="%s" width="300"/>' % obj.url.url)
        else:
            return 'No Image Found'

    cetrificate_img.allow_tags = True
    cetrificate_img.short_description = 'Фотография сертификата'

    list_display = ('title', 'subt', 'cetrificate_img',)
