from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Report
from .serializers import ReportSerializer
from .tasks import generate_report


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    filterset_fields = ["report_type", "status", "campaign"]

    def get_queryset(self):
        return Report.objects.filter(generated_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(generated_by=self.request.user)

    @action(detail=True, methods=["post"])
    def generate(self, request, pk=None):
        report = self.get_object()
        generate_report.delay(report.id)
        return Response(
            {"status": "Report generation started"},
            status=status.HTTP_202_ACCEPTED,
        )
