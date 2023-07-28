# restframework - django
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

# App
from apps.event.models import Event, EventStatus, EventType
from apps.event.api.serializer import EventSerializer
from apps.status.api.serializer import EventStatusSerializer
from apps.type.api.serializer import EventTypeSerializer

class EventViewSet(viewsets.ModelViewSet):
    """Event view set."""
    queryset = Event.objects.filter(is_deleted=False)
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if 'description' not in request.data:
            raise serializers.ValidationError("El campo 'description' es obligatorio.")
        
        if 'date' not in request.data:
            raise serializers.ValidationError("El campo 'date' es obligatorio.")

        if 'type' not in request.data:
            raise serializers.ValidationError("El campo 'type' es obligatorio.")

        event_type = EventType.objects.get(id=request.data['type'])
        event_status = EventStatus.objects.get(id=1)

        event = Event.objects.create(
            description=request.data['description'],
            date=request.data['date'],
            type=event_type,
            status=event_status,
        )

        serializer = self.get_serializer(instance=event)
        response = Response(serializer.data, status=status.HTTP_201_CREATED)
        return response
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Cambio de estado
        if 'status' in request.data:
            if request.data['type'] != "2" and request.data['status'] == "2":
                if instance.type.id != 2:
                    if 'requires_management' not in request.data or request.data['requires_management'] == None:
                        raise serializers.ValidationError(
                            "El campo 'requires_management' es obligatorio para Eventos de tipo 1 o 3."
                        )

        # Control de la instancia
        if instance.type.id != 2 and instance.requires_management is None:
            serializer.validated_data['status'] = EventStatus.objects.get(id=1)

        # Creacion de las instancias
        if 'status' in request.data:
            serializer.validated_data['status'] = EventStatus.objects.get(id=request.data['status'])

        if 'type' in request.data:
            if request.data['type'] != "2":
                if instance.status.id == 2:
                    serializer.validated_data['status'] = EventStatus.objects.get(id=1)
                    serializer.validated_data['requires_management'] = None
            if instance.status.id == 2:
                    serializer.validated_data['requires_management'] = None
            serializer.validated_data['type'] = EventType.objects.get(id=request.data['type'])

        if 'is_deleted' in request.data:
            raise serializers.ValidationError("El campo 'is_deleted' no se puede modificar.")

        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Cambio de estado
        if 'status' in request.data:
            if request.data['type'] != "2" and request.data['status'] == "2":
                if instance.type.id != 2:
                    if 'requires_management' not in request.data or request.data['requires_management'] == None:
                        raise serializers.ValidationError(
                            "El campo 'requires_management' es obligatorio para Eventos de tipo 1 o 3."
                        )

        # Control de la instancia
        if instance.type.id != 2 and instance.requires_management is None:
            serializer.validated_data['status'] = EventStatus.objects.get(id=1)

        # Creacion de las instancias
        if 'status' in request.data:
            serializer.validated_data['status'] = EventStatus.objects.get(id=request.data['status'])

        if 'type' in request.data:
            if request.data['type'] != "2":
                if instance.status.id == 2:
                    serializer.validated_data['status'] = EventStatus.objects.get(id=1)
                    serializer.validated_data['requires_management'] = None
            if instance.status.id == 2:
                    serializer.validated_data['requires_management'] = None
            serializer.validated_data['type'] = EventType.objects.get(id=request.data['type'])

        if 'is_deleted' in request.data:
            raise serializers.ValidationError("El campo 'is_deleted' no se puede modificar.")

        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=204)