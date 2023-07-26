import time

# restframework
from rest_framework import viewsets, status
from rest_framework.response import Response

# App
from apps.event.models import Event
from apps.event.api.serializer import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """Event view set."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    model = Event