# mascotas/urls.py

from django.urls import path
from .views import listar_mascotas_view

urlpatterns = [
    path('', listar_mascotas_view, name='listar_mascotas'),  # Asignando la vista al URL raíz
]
