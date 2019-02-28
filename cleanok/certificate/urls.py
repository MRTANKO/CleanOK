"""Менеджер URL-ов приложения certificate."""
from django.urls import path

from .views import Certificates

urlpatterns = [
    path('', Certificates.as_view()),
]
