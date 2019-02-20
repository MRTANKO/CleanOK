from .models import Vacancy
from .serializers import VacancySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class Vacancys(generics.ListAPIView):
    """Вакансии API"""
    queryset = Vacancy.objects
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        vacancys = Vacancy.objects.all()
        serializer = VacancySerializer(vacancys, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)
