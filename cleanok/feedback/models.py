"""Модели приложения feedback."""
from django.db import models


class Message(models.Model):
    """Модель сообщений."""

    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    message = models.TextField('Сообщение')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
