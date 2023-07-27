from rest_framework import serializers
from apps.event.models import Event, EventType, EventStatus

class EventSerializer(serializers.ModelSerializer):
    type = serializers.PrimaryKeyRelatedField(queryset=EventType.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=EventStatus.objects.all())

    class Meta:
        model = Event
        fields = ['id', 'description', 'date', 'management', 'type', 'status', 'isdeleted']