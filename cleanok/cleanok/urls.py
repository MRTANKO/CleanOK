"""cleanok URL Configuration."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('galleries/', include('gallery.urls')),
    path('certificates/', include('certificate.urls')),
    path('recomends/', include('recomend.urls')),
    path('promos/', include('promo.urls')),
    path('services/', include('services.urls')),
    path('vacancies/', include('vacancy.urls')),
    path('news/', include('news.urls')),
    path('feedbacks/', include('feedback.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
