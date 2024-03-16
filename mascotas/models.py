from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    dueño = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
