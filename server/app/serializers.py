from rest_framework import serializers

from .models import AuthMessage


class AuthMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthMessage
        fields = ("pk", "creation_date", "clear_message", "encrypted_message")
