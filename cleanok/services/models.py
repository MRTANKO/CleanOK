"""Модели приложения services."""
from django.db import models

from .validators import validate_phone, validate_price


class Item(models.Model):
    """Модель пунктов работы."""

    name = models.TextField('Название пункта работы')

    def __str__(self):
        """Перевод пункта в строковый тип для отображения в админке."""
        return self.name

    class Meta:
        """Настройки модели."""

        verbose_name = 'Пункт работы'
        verbose_name_plural = 'Пункты работы'


class Category(models.Model):
    """Модель категорий."""

    def __str__(self):
        """Перевод категории в строковый тип для отображения в админке."""
        return self.name

    name = models.CharField('Название категории', max_length=30)

    class Meta:
        """Настройки модели."""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    """Модель услуг."""

    def __str__(self):
        """Перевод названия услуги в строковый тип."""
        return self.name

    category = models.ForeignKey(
        Category,
        verbose_name='Категория услуги',
        on_delete=models.CASCADE
    )
    name = models.CharField('Название услуги', max_length=30)
    desc = models.TextField('Комментарий к услуге')
    items = models.ManyToManyField(
        Item,
        verbose_name='Пункты работы',
        related_name='items_service'
    )
    price = models.IntegerField(
        'Минимальная цена', validators=[validate_price])
    note = models.TextField('Примечание')
    warn = models.TextField('Предупреждение')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Request(models.Model):
    """Модель запросов."""

    name = models.CharField('Имя', max_length=30)
    phone = models.CharField(
        'Телефон', max_length=30, validators=[validate_phone])
    service = models.ForeignKey(
        Service, verbose_name='Услуга', on_delete=models.CASCADE)
    comment = models.TextField('Комментарий')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
