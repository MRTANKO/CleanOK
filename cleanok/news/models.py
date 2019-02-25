"""Модели приложения news."""
from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    """Модель новостей."""

    date = models.DateField('Дата публикации')
    title = models.CharField('Заголовок', max_length=30)
    preview = models.TextField('Содержание')
    text = RichTextField('Текст')
    related = models.ManyToManyField(
        'self',
        verbose_name='Ссылки на другие новости',
        related_name='items_news',
        blank=True
    )

    def __str__(self):
        """Перевод заголовка в строковый тип для отображения в админке."""
        return self.title

    class Meta:
        """Настройки модели."""

        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
