"""Менеджер URL-ов приложения vacancy."""
from django.urls import path

from .views import Vacancies

urlpatterns = [
    path('', Vacancies.as_view()),
]
