"""Модели приложения certificate."""
from django.db import models


class Certificate(models.Model):
    """Модель сертификата."""

    url = models.ImageField('Фотография сертификата', upload_to='certificate')
    title = models.CharField('Название сертификата', max_length=30)
    subt = models.CharField('Компания', max_length=30)

    class Meta:
        """Настройки модели."""

        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
