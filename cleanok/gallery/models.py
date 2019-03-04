"""Модели приложения gallery."""
from django.db import models


class Image(models.Model):
    """Модель фотографии."""

    img = models.ImageField('Фотография', upload_to='gallery')

    def __str__(self):
        """Перевод фотографии в строковый тип для отображения в админке."""
        return str(self.img)

    class Meta:
        """Настройки модели."""

        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Group(models.Model):
    """Модель фотоальбома."""

    title = models.CharField('Название альбома', max_length=30)
    cover = models.ImageField('Фото на фон', upload_to='Gallery')
    items = models.ManyToManyField(
        Image, verbose_name='Фотографии', related_name='items_image')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
