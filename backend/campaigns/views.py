from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from analytics.models import MetricSnapshot
from analytics.utils import aggregate_metrics, compute_analytics_with_trends, get_period_querysets, parse_days_param
from cortex.ml_client import ml_service_post
from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    filterset_fields = ["status", "platform"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "name", "budget"]

    def get_queryset(self):
        return Campaign.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=["get"])
    def analytics(self, request, pk=None):
        """GET /campaigns/{id}/analytics/?days=30"""
        campaign = self.get_object()
        days = parse_days_param(request)

        base_qs = MetricSnapshot.objects.filter(campaign=campaign)
        current_qs, previous_qs = get_period_querysets(base_qs, days)

        current = aggregate_metrics(current_qs)
        previous = aggregate_metrics(previous_qs)

        result = compute_analytics_with_trends(current, previous)
        result["period_days"] = days

        return Response(result)

    @action(detail=True, methods=["post"])
    def insights(self, request, pk=None):
        """POST /campaigns/{id}/insights/ — AI-powered campaign insights."""
        campaign = self.get_object()
        days = parse_days_param(request)

        base_qs = MetricSnapshot.objects.filter(campaign=campaign)
        current_qs, previous_qs = get_period_querysets(base_qs, days)

        current = aggregate_metrics(current_qs)
        previous = aggregate_metrics(previous_qs)

        analytics_data = compute_analytics_with_trends(current, previous)
        analytics_data["campaign_name"] = campaign.name
        analytics_data["platform"] = campaign.platform
        analytics_data["status"] = campaign.status

        return ml_service_post("/api/v1/insights/campaign", analytics_data)
