from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "organization", "role", "created_at"]
        read_only_fields = ["id", "created_at", "role"]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Extends the default token response to include user profile fields."""

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["email"] = self.user.email
        data["role"] = self.user.role
        data["organization"] = self.user.organization
        return data
