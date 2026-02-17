from rest_framework import serializers

from .models import MetricSnapshot


class MetricSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricSnapshot
        fields = [
            "id", "campaign", "date", "impressions", "clicks",
            "conversions", "spend", "revenue", "ctr", "roas", "created_at",
        ]
        read_only_fields = ["id", "ctr", "roas", "created_at"]
