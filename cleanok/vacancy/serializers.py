"""Сериализатор приложения vacancy."""
from rest_framework import serializers

from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    """Сериализация вакансии."""

    salary = serializers.SerializerMethodField('salary_str')

    @staticmethod
    def salary_str(obj):
        """Форматирование зарплаты."""
        return 'от {} рублей'.format(obj.salary)

    class Meta:
        """Настройки сериализатора."""

        model = Vacancy
        fields = (
            'id', 'job', 'salary', 'loc', 'req', 'resp', 'cond', 'contact')
