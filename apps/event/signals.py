from django.db.models.signals import post_migrate
from django.dispatch import receiver
from apps.event.models import Event
from apps.status.models import EventStatus
from apps.type.models import EventType

@receiver(post_migrate)
def create_default_events(sender, **kwargs):

    if EventType.objects.count() == 0:
        EventType.objects.create(name="Evento tipo 1")
        EventType.objects.create(name="Evento tipo 2")
        EventType.objects.create(name="Evento tipo 3")
    
    if EventStatus.objects.count() == 0:
        EventStatus.objects.create(name="Pendiente")
        EventStatus.objects.create(name="Revisado")

    if Event.objects.count() == 0:
        Event.objects.create(
            description='Boda de los Martinez',
            date='2023-08-01',
            type=EventType.objects.get(id=1),
            status=EventStatus.objects.get(id=1)
        )
        Event.objects.create(
            description='15 años de los Ortiz',
            date='2023-09-12',
            type=EventType.objects.get(id=2),
            status=EventStatus.objects.get(id=1)
        )
        Event.objects.create(
            description='Bautizo de Milena',
            date='2023-08-12',
            type=EventType.objects.get(id=3),
            status=EventStatus.objects.get(id=1)
        )