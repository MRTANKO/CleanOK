from django.db import models


class Image(models.Model):
    """Модель фотографии"""
    img = models.ImageField('Фотография', upload_to='Gallery')

    def __str__(self):
        """Перевод данных в строковый тип для отображения в админке"""
        return str(self.img)

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'


class Group(models.Model):
    """Модель группы(фотоальбома)"""
    title = models.TextField('Название альбома')
    cover = models.ImageField('Фото на фон', upload_to='Gallery')
    items = models.ManyToManyField(Image, verbose_name='Фотографии', related_name='items_image')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
