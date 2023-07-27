from rest_framework import serializers
from apps.status.models import EventStatus

class EventStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ('id', 'name')