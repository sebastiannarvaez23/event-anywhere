from django.shortcuts import render
from rest_framework import viewsets
from apps.type.api.serializer import EventTypeSerializer
from apps.type.models import EventType

# Create your views here.
class EventTypeViewSet(viewsets.ModelViewSet):
    """EventType view set."""
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer