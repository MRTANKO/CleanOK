from django.urls import path
from .views import Vacancys

urlpatterns = [
    path('', Vacancys.as_view()),
]
