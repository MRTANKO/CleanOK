from django.db import models


class Vacancy(models.Model):
    """Модель вакансии"""
    job = models.CharField('Название вакансии', max_length=30)
    salary = models.IntegerField('Зарплата')
    loc = models.CharField('Города, где требуется', max_length=50)
    req = models.TextField('Требования')
    resp = models.TextField('Основные обязанности')
    cond = models.TextField('Предлагаем')
    contact = models.TextField('Контакты')

    class Meta:
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'
