from rest_framework import viewsets

from .models import AuthMessage
from .serializers import AuthMessageSerializer


class AuthMessageViewSet(viewsets.ModelViewSet):
    queryset = AuthMessage.objects.all().order_by("creation_date")
    serializer_class = AuthMessageSerializer
