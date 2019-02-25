"""Администрирование приложения gallery."""
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Group, Image


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Редактирование альбомов."""

    def image_tag(self, obj):
        """Получение картинки."""
        if obj.cover:
            return mark_safe('<img src="%s" width="300"/>' % obj.cover.url)
        else:
            return 'No Image Found'

    image_tag.allow_tags = True
    image_tag.short_description = 'Фотография на фон'

    list_display = ('title', 'image_tag',)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Редактирование фотографии."""

    def image_img(self, obj):
        """Получение фотографии."""
        if obj.img:
            return mark_safe('<img src="%s" width="300"/>' % obj.img.url)
        else:
            return 'Image not found'

    def image_name(self, obj):
        """Получение имени фотографии."""
        if obj.img:
            return str(obj.img)
        else:
            return 'Image not found'

    image_img.allow_tags = True
    image_img.short_description = 'Фотография'

    image_name.allow_tags = True
    image_name.short_description = 'Название фотографии'

    list_display = ('image_img', 'image_name')
