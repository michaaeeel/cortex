from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            "id", "title", "report_type", "campaign",
            "generated_by", "content", "status", "created_at",
        ]
        read_only_fields = ["id", "content", "status", "created_at"]
