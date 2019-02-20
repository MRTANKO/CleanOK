from django.urls import path
from .views import News

urlpatterns = [
    path('', News.as_view()),
]