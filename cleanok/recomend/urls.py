"""Менеджер URL-ов приложения recomend."""
from django.urls import path

from .views import Recomends

urlpatterns = [
    path('', Recomends.as_view()),
]
