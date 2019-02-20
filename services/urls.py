from django.urls import path
from .views import Services, CategoryAPI, RequestAPI, MessageAPI

urlpatterns = [
    path('services', Services.as_view()),
    path('', CategoryAPI.as_view()),
    path('leads', RequestAPI.as_view()),
    path('feedback', MessageAPI.as_view())
]
