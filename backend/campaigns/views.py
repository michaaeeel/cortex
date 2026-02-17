from rest_framework import viewsets

from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filterset_fields = ["status", "platform"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "name", "budget"]
