from django.contrib import admin

from .models import DataSource


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ["name", "source_type", "is_active", "last_sync_at", "owner"]
    list_filter = ["source_type", "is_active"]
