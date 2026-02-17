from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MetricSnapshot
from .serializers import MetricSnapshotSerializer


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

        aggregates = qs.aggregate(
            total_impressions=Sum("impressions"),
            total_clicks=Sum("clicks"),
            total_conversions=Sum("conversions"),
            total_spend=Sum("spend"),
            total_revenue=Sum("revenue"),
        )

        return Response(aggregates)
