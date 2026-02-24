from rest_framework import viewsets

from .models import DataSource
from .serializers import DataSourceSerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    serializer_class = DataSourceSerializer
    filterset_fields = ["source_type", "is_active"]
    search_fields = ["name"]

    def get_queryset(self):
        return DataSource.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
