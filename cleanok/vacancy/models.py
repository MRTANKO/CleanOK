"""Модели приложения vacancy."""

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Vacancy(models.Model):
    """Модель вакансии."""

    def validate_salary(value):
        """Проверяет валидность зарплаты."""
        if value <= 0:
            raise ValidationError(
                _('%(value)s некоректная зарплата'),
                params={'value': value},
            )

    job = models.CharField('Название вакансии', max_length=30)
    salary = models.IntegerField('Зарплата', validators=[validate_salary])
    loc = models.CharField('Города, где требуется', max_length=50)
    req = models.TextField('Требования')
    resp = models.TextField('Основные обязанности')
    cond = models.TextField('Предлагаем')
    contact = models.TextField('Контакты')

    class Meta:
        """Настройки модели."""

        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'
