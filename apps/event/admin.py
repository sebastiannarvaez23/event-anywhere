from django.contrib import admin
from apps.event.models import Event, EventStatus, EventType

# Register your models here.
admin.site.register(Event)