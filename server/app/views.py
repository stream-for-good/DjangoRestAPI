from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AuthMessageSerializer
from .models import AuthMessage


class AuthMessageViewSet(viewsets.ModelViewSet):
    queryset = AuthMessage.objects.all()
    # queryset = AuthMessage.objects.all().order_by('date')
    serializer_class = AuthMessageSerializer
