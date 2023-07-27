from django.shortcuts import render
from rest_framework import viewsets
from apps.status.api.serializer import EventStatusSerializer
from apps.status.models import EventStatus

# Create your views here.

class EventStatusViewSet(viewsets.ModelViewSet):
    """EventStatus view set."""
    queryset = EventStatus.objects.filter(is_deleted=False)
    serializer_class = EventStatusSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=204)