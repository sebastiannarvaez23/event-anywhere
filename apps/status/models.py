from django.db import models

# Create your models here.
class EventStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    is_deleted = models.BooleanField(default=False, verbose_name="Eliminado")

    class Meta:
        verbose_name = "Estado del Evento"
        verbose_name_plural = "Estados de los eventos"
        ordering = ['-id']

    def __str__(self):
        return self.name