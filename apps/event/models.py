from django.db import models

# Create your models here.
class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name

class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")

    class Meta:
        verbose_name = "Estado del Evento"
        verbose_name_plural = "Estados de los eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name

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
