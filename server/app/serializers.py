from rest_framework import serializers

from .models import AuthMessage


class AuthMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthMessage
        fields = ("clear_message", "encrypted_message", "creation_date")
