# mascotas/views.py

from django.shortcuts import render
from .models import Mascota
from .tasks import listar_mascotas
from django.conf import settings


def listar_mascotas_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        raza = request.POST.get('raza')
        dueño = request.POST.get('dueño')

        listar_mascotas.delay(nombre, raza, dueño)

    mascotas = Mascota.objects.all()
    broker = settings.CELERY_BROKER_URL
    backend = settings.CELERY_RESULT_BACKEND
    return render(request, 'listar_mascotas.html', {'mascotas': mascotas, 'backend':backend, 'broker': broker})
