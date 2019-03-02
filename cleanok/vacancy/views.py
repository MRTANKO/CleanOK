"""Представления приложения vacancy."""
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Vacancy
from .serializers import VacancySerializer


class Vacancies(generics.ListAPIView):
    """API вакансий."""

    queryset = Vacancy.objects.all()
    pagination_class = PageNumberPagination
    serializer_class = VacancySerializer
