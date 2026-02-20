from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/token/", CustomTokenObtainPairView.as_view(), name="token_obtain"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/campaigns/", include("campaigns.urls")),
    path("api/v1/data-sources/", include("data_sources.urls")),
    path("api/v1/analytics/", include("analytics.urls")),
    path("api/v1/reports/", include("reports.urls")),
]
