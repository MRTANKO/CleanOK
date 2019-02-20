from django.urls import path
from .views import Sertificates

urlpatterns = [
    path('', Sertificates.as_view()),
]