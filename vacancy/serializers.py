from rest_framework import serializers
from .models import Vacancy


class VacancySerializer(serializers.ModelSerializer):
    """Сериализация вакансии"""
    salary = serializers.SerializerMethodField('salary_ser')

    @staticmethod
    def salary_ser(obj):
        """Формаирование зарплаты"""
        return 'от {} рублей'.format(obj.salary)

    class Meta:
        model = Vacancy
        fields = ('id', 'job', 'salary', 'loc', 'req', 'resp', 'cond', 'contact')
