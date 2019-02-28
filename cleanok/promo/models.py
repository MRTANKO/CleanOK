"""Модели приложения promo."""
from django.db import models


class Promo(models.Model):
    """Модель акции."""

    title = models.CharField('Название акции', max_length=50)
    preview = models.TextField('Описание акции')
    date = models.DateField('Дата публикации')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Акцию'
        verbose_name_plural = 'Акции'
