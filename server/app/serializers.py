from rest_framework import serializers

from .models import AuthToken


class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthToken
        fields = ("pk", "creation_date", "clear_message", "encrypted_message")
