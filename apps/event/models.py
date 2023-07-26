from django.db import models

# Create your models here.
class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name

class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Estado del Evento"
        verbose_name_plural = "Estados de los eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    date = models.DateField()
    management = models.BooleanField()
    type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(EventStatus, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-id']
