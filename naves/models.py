from django.db import models

# Create your models here.
class Nave(models.Model):


    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:

        return self.nombre

    class Meta:
        verbose_name = "descripcion de nave"
        verbose_name_plural = "descripciones de naves"
