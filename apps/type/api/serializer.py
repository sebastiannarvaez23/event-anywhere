from rest_framework import serializers
from apps.type.models import EventType

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ('id', 'name')