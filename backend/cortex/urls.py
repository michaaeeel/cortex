from django.contrib import admin
from django.urls import include, path
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.serializers import CustomTokenObtainPairSerializer


class AuthRateThrottle(AnonRateThrottle):
    rate = "5/min"


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    throttle_classes = [AuthRateThrottle]


class LogoutView(APIView):
    """POST /api/v1/auth/logout/ — blacklist the supplied refresh token."""

    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Refresh token required."}, status=400)
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            return Response({"detail": "Token is invalid or already blacklisted."}, status=400)
        return Response(status=205)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/token/", CustomTokenObtainPairView.as_view(), name="token_obtain"),
    path("api/v1/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/auth/logout/", LogoutView.as_view(), name="logout"),
    path("api/v1/users/", include("users.urls")),
    path("api/v1/campaigns/", include("campaigns.urls")),
    path("api/v1/data-sources/", include("data_sources.urls")),
    path("api/v1/analytics/", include("analytics.urls")),
    path("api/v1/reports/", include("reports.urls")),
]
