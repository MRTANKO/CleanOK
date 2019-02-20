from django.contrib import admin
from .models import Recomend
from django.utils.safestring import mark_safe


@admin.register(Recomend)
class RecAdmin(admin.ModelAdmin):
    """Редактирование рекомендаций"""

    def usl_img(self, obj):
        if obj.usl:
            return mark_safe('<img src="%s" width="300"/>' % obj.usl.url)
        else:
            return 'No Image Found'

    usl_img.allow_tags = True
    usl_img.short_description = 'Фотография'

    list_display = ('title', 'usl_img', 'year')
