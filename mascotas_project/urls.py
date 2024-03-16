# mascotas_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mascotas.urls')),  # Incluyendo las URLs de la aplicación mascotas
    path('admin/', admin.site.urls),
]
