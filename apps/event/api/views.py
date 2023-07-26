# restframework - django
from rest_framework import viewsets, status
from rest_framework.response import Response

# App
from apps.event.models import Event, EventStatus, EventType
from apps.event.api.serializer import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    """Event view set."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
"""
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        event_status = EventStatus.objects.get(id=request.data['status'])
        event_type = EventType.objects.get(id=request.data['type'])
        
        event = Event.objects.create(
            description=request.data['description'],
            date=request.data['date'],
            management=request.data['management'],
            type=event_type,
            status=event_status,
        )

        serializer = self.get_serializer(instance=event)
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return response """