from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Mems

@admin.register(Mems)
class MemsAdmin(admin.ModelAdmin):
    def get_image(self, Mems):
        return mark_safe(f'<img width="50px" src="{Mems.img.url}" alt="{Mems.name}" class="admin-icon"/>')

    get_image.short_description = u'Привью'
    list_display = ('name', 'get_image')



