from django.contrib import admin
from django.urls import path, include

apiversion = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{apiversion}event/', include('apps.event.api.urls')),
]