from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.event.api.views import EventViewSet

router = DefaultRouter()
router.register(r'', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]