from django.shortcuts import render
from rest_framework import viewsets
from apps.type.api.serializer import EventTypeSerializer
from apps.type.models import EventType

# Create your views here.
class EventTypeViewSet(viewsets.ModelViewSet):
    """EventType view set."""
    queryset = EventType.objects.filter(is_deleted=False)
    serializer_class = EventTypeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=204)