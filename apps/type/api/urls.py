from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.type.api.views import EventTypeViewSet

routerType = DefaultRouter()
routerType.register(r'', EventTypeViewSet, basename='type')

urlpatterns = [
    path('', include(routerType.urls)),
]