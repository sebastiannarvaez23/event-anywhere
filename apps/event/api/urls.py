from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.event.api.views import EventViewSet
from apps.status.api.views import EventStatusViewSet
from apps.type.api.views import EventTypeViewSet

routerEvent = DefaultRouter()
routerEvent.register(r'', EventViewSet, basename='event')

routerType = DefaultRouter()
routerType.register(r'', EventTypeViewSet, basename='type')

routerStatus = DefaultRouter()
routerStatus.register(r'', EventStatusViewSet, basename='status')

urlpatterns = [
    path('', include(routerEvent.urls)),
    path('type/', include(routerType.urls)),
    path('status/', include(routerStatus.urls)),
]