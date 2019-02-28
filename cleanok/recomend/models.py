"""Модели приложения recomend."""
import datetime

from django.db import models


class Recomend(models.Model):
    """Модель рекомендаций."""

    yearchoices = [(r, r) for r in range(1980, datetime.date.today().year + 1)]

    url = models.ImageField('Фотография сертификата', upload_to='recomend')
    title = models.CharField('Название организации', max_length=30)
    year = models.IntegerField(
        'Год',
        choices=yearchoices,
        default=datetime.datetime.now().year
    )

    class Meta:
        """Настройки модели."""

        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'
