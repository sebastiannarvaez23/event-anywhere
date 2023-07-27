from django.db import models
from apps.status.models import EventStatus
from apps.type.models import EventType

# Create your models here.
class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, verbose_name="Descripción")
    date = models.DateField(verbose_name="Fecha del evento")
    requires_management = models.BooleanField(blank=True, null=True, default=None, verbose_name="Requiere gestión")
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado")
    type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING, verbose_name="Tipo de Evento")
    status = models.ForeignKey(EventStatus, on_delete=models.DO_NOTHING, verbose_name="Estado del Evento")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-id']
