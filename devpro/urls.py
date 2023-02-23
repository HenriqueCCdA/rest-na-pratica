from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('devpro.core.urls')),
    path('api/v2/', include('devpro.api2.urls'))
]
