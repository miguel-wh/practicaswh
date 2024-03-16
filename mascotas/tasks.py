# mascotas/tasks.py

from celery import shared_task
from .models import Mascota

@shared_task
def listar_mascotas(nombre, raza, dueño):
    Mascota.objects.create(nombre=nombre, raza=raza, dueño=dueño)
    return "Mascota creada"
