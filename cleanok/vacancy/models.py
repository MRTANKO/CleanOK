"""Модели приложения vacancy."""
from django.db import models

from .validators import validate_salary


class Vacancy(models.Model):
    """Модель вакансии."""

    job = models.CharField('Название вакансии', max_length=30)
    salary = models.IntegerField('Зарплата', validators=[validate_salary])
    loc = models.CharField('Города, где требуется', max_length=50)
    req = models.TextField('Требования')
    resp = models.TextField('Основные обязанности')
    cond = models.TextField('Предлагаем')
    contact = models.TextField('Контакты')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
