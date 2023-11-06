from django.contrib import admin
from .models import Common
from django.utils.safestring import mark_safe

@admin.register(Common)
class ReceptsAdmin(admin.ModelAdmin):
    def get_image(self, Common):
        return mark_safe(f'<img width="50px" '
                         f'src="{Common.img.url}" '
                         f'alt="{Common.name}" '
                         f'class="admin-icon"/>')
    list_display = ('name', 'get_image')
    list_display_links = list_display
    get_image.short_description = u'Привью'
    search_fields = ('name',)
    search_help_text = f"Search fields: {', '.join(search_fields)}"
