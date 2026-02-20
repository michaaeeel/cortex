from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MeView(APIView):
    """GET /api/v1/users/me/ — return the current authenticated user's profile."""

    def get(self, request):
        return Response(UserSerializer(request.user).data)
