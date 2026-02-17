from django.contrib import admin

from .models import MetricSnapshot


@admin.register(MetricSnapshot)
class MetricSnapshotAdmin(admin.ModelAdmin):
    list_display = ["campaign", "date", "impressions", "clicks", "spend", "revenue", "ctr", "roas"]
    list_filter = ["date", "campaign"]
