from rest_framework import serializers
from apps.event.models import Event

class EventSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d", required=False)
    status = serializers.CharField(source='status.name', required=False)
    
    class Meta:
        model = Event
        fields = ('id', 'description', 'date', 'management', 'type', 'status',)