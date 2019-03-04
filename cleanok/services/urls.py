"""Менеджер URL-ов приложения services."""
from django.urls import path

from .views import Services, CategoryAPI, RequestAPI

urlpatterns = [
    path('', Services.as_view()),
    path('categories/', CategoryAPI.as_view()),
    path('leads/', RequestAPI.as_view()),
]
