from django.contrib import admin
from .models import New


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    """Редактирвание новости"""

    list_display = ('title', 'date', 'preview')
