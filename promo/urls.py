from django.urls import path
from .views import Promos

urlpatterns = [
    path('', Promos.as_view()),
]