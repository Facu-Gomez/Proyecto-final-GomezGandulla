from django.db import models
from planeta.models import Planeta

class Personaje(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    planeta_origen_id = models.ForeignKey(
        Planeta, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="planeta de origen"
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    

