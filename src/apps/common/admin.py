from django.contrib import admin
from apps.common.models import Anekdot


@admin.register(Anekdot)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = list_display

    search_fields = ('name',)
    search_help_text = f"Search fields: {', '.join(search_fields)}"
