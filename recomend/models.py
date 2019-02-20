from django.db import models
import datetime


class Recomend(models.Model):
    """Модель рекомендаций"""
    yearchoices = [(r, r) for r in range(1980, datetime.date.today().year + 1)]

    usl = models.ImageField('Фотография сертификата', upload_to='Recomend')
    title = models.TextField('Название организации')
    year = models.IntegerField('Год', choices=yearchoices, default=datetime.datetime.now().year)

    class Meta:
        verbose_name = 'Рекомендация'
        verbose_name_plural = 'Рекомендации'
