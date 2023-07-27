from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.status.api.views import EventStatusViewSet

routerStatus = DefaultRouter()
routerStatus.register(r'', EventStatusViewSet, basename='status')

urlpatterns = [
    path('', include(routerStatus.urls)),
]