from django.urls import path
from apps.event.api.views import EventViewSet

urlpatterns = [
    path('', EventViewSet.as_view({'get': 'list'})),
]