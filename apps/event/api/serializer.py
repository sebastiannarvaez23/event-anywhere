from rest_framework import serializers
from apps.event.models import Event, EventType, EventStatus

class EventSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Event
        fields = ['id', 'description', 'date', 'requires_management', 'type', 'status']