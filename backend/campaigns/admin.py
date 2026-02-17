from django.contrib import admin

from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "platform", "budget", "owner", "created_at"]
    list_filter = ["status", "platform"]
    search_fields = ["name"]
