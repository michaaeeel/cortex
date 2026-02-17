from django.conf import settings
from django.db import models


class DataSource(models.Model):
    SOURCE_TYPES = [
        ("google_ads", "Google Ads"),
        ("meta_ads", "Meta Ads"),
        ("google_analytics", "Google Analytics"),
    ]

    name = models.CharField(max_length=255)
    source_type = models.CharField(max_length=50, choices=SOURCE_TYPES)
    credentials = models.JSONField(default=dict, blank=True)
    is_active = models.BooleanField(default=True)
    last_sync_at = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="data_sources",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_source_type_display()})"

    class Meta:
        ordering = ["-created_at"]
