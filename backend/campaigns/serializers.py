from rest_framework import serializers

from .models import Campaign


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            "id", "name", "description", "status", "platform",
            "budget", "start_date", "end_date", "owner", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
