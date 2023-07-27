from django.shortcuts import render
from rest_framework import viewsets
from apps.status.api.serializer import EventStatusSerializer
from apps.status.models import EventStatus

# Create your views here.

class EventStatusViewSet(viewsets.ModelViewSet):
    """EventStatus view set."""
    queryset = EventStatus.objects.all()
    serializer_class = EventStatusSerializer