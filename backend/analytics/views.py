from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from campaigns.models import Campaign
from cortex.ml_client import ml_service_post
from .models import MetricSnapshot
from .serializers import MetricSnapshotSerializer
from .utils import aggregate_metrics, compute_derived_metrics, calculate_trend, get_period_querysets, parse_days_param


class MetricSnapshotViewSet(viewsets.ModelViewSet):
    queryset = MetricSnapshot.objects.all()
    serializer_class = MetricSnapshotSerializer
    filterset_fields = ["campaign", "date"]
    ordering_fields = ["date", "spend", "revenue"]

    @action(detail=False, methods=["get"])
    def summary(self, request):
        campaign_id = request.query_params.get("campaign_id")
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")

        qs = self.get_queryset()
        if campaign_id:
            qs = qs.filter(campaign_id=campaign_id)
        if start_date:
            qs = qs.filter(date__gte=start_date)
        if end_date:
            qs = qs.filter(date__lte=end_date)

        return Response(aggregate_metrics(qs))

    @action(detail=False, methods=["get"])
    def dashboard(self, request):
        """GET /analytics/metrics/dashboard/?days=30"""
        days = parse_days_param(request)

        current_qs, previous_qs = get_period_querysets(MetricSnapshot.objects.all(), days)
        current = aggregate_metrics(current_qs)
        previous = aggregate_metrics(previous_qs)
        derived = compute_derived_metrics(current)

        return Response({
            "active_campaigns": Campaign.objects.filter(status="active").count(),
            "total_campaigns": Campaign.objects.count(),
            **current,
            **derived,
            "period_days": days,
            "trends": {
                "spend": calculate_trend(current["spend"], previous["spend"]),
                "revenue": calculate_trend(current["revenue"], previous["revenue"]),
                "impressions": calculate_trend(current["impressions"], previous["impressions"]),
                "clicks": calculate_trend(current["clicks"], previous["clicks"]),
            },
        })

    @action(detail=False, methods=["post"], url_path="dashboard/insights")
    def dashboard_insights(self, request):
        """POST /analytics/metrics/dashboard/insights/ — AI-powered dashboard insights."""
        return ml_service_post("/api/v1/insights/dashboard", request.data)
