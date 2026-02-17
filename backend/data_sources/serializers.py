from rest_framework import serializers

from .models import DataSource


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = [
            "id", "name", "source_type", "is_active",
            "last_sync_at", "owner", "created_at",
        ]
        read_only_fields = ["id", "last_sync_at", "created_at"]
