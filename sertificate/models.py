from django.db import models


class Sertificate(models.Model):
    """Модель сертификата"""
    usl = models.ImageField('Фотография сертификата', upload_to='Sertificate')
    title = models.CharField('Название сертификата', max_length=30)
    subt = models.CharField('Компания', max_length=30)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'
