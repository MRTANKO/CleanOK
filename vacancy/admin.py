from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Редактирвание вакансии"""

    list_display = ('job', 'salary', 'loc', 'req', 'resp', 'cond', 'contact')
