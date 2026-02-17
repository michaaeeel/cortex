from rest_framework import viewsets

from .models import DataSource
from .serializers import DataSourceSerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer
    filterset_fields = ["source_type", "is_active"]
    search_fields = ["name"]
