from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


class Item(models.Model):
    """Модель пунктов работы"""
    name = models.TextField('Название пункта работы')

    def __str__(self):
        """Перевод данных в строковый тип для отображения в админке"""
        return self.name

    class Meta:
        verbose_name = 'Пункт работы'
        verbose_name_plural = 'Пункты работы'


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField('Название категории', max_length=30)

    def __str__(self):
        """Перевод данных в строковый тип для отображения в админке"""
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Service(models.Model):
    """Модель услуг"""
    category = models.ForeignKey(Category, verbose_name='Категория услуги', on_delete=models.CASCADE)
    name = models.CharField('Название услуги', max_length=30)
    desc = models.TextField('Комментарий к услуге')
    items = models.ManyToManyField(Item, verbose_name='Пункты работы', related_name='items_service')
    price = models.IntegerField('Минимальная цена')
    note = models.TextField('Примечание')
    warn = models.TextField('Предупреждение')

    def __str__(self):
        """Перевод данных в строковый тип для отображения в админке"""
        return self.name

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'


class Request(models.Model):
    """Модель запросов"""
    def validate_even(value):
        if not re.fullmatch('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', value):
            raise ValidationError(
                _('%(value)s некоректный номер телефона'),
                params={'value': value},
            )

    name = models.CharField('Имя', max_length=30)
    phone = models.CharField('Телефон', max_length=30, validators=[validate_even])
    service = models.ForeignKey(Service, verbose_name='Услуга', on_delete=models.CASCADE)
    comment = models.TextField('Комментарий')

    class Meta:
        verbose_name = 'Запрс'
        verbose_name_plural = 'Запросы'


class Message(models.Model):
    """Модель сообщений"""
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    message = models.TextField('Сообщение')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

