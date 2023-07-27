from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from apps.type.api.serializer import EventTypeSerializer
from apps.type.models import EventType

# Create your views here.
class EventTypeViewSet(viewsets.ModelViewSet):
    """EventType view set."""
    queryset = EventType.objects.filter(is_deleted=False)
    serializer_class = EventTypeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        if 'is_deleted' in request.data:
            raise serializers.ValidationError("El campo 'is_deleted' no se puede modificar.")

        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        if 'is_deleted' in request.data:
            raise serializers.ValidationError("El campo 'is_deleted' no se puede modificar.")

        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=204)