from django.db import models

class Planeta(models.Model):


    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:
        """Representa una instancia del modelo como una cadena de texto"""
        return self.nombre

    class Meta:
        verbose_name = "descripcion de planetas"
        verbose_name_plural = "descripciones de planetas"