from django.contrib import admin
from django.urls import path, include

# Swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


apiversion = 'api/v1/'

schema_view = get_schema_view(
   openapi.Info(
      title="Event Anywhere",
      default_version='v1',
      description="Esta aplicación te permite registrar eventos y administrarlos.",
      terms_of_service="",
      contact=openapi.Contact(email="narvaezsebas8@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    # Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Paths app
    path('admin/', admin.site.urls),
    path(f'{apiversion}event/', include('apps.event.api.urls')),
    path(f'{apiversion}status/', include('apps.status.api.urls')),
    path(f'{apiversion}type/', include('apps.type.api.urls')),
]