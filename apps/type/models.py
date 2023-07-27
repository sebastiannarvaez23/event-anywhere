from django.db import models

# Create your models here.
class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado")

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name