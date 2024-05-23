from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Planeta(models.Model):


    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "descripcion de planetas"
        verbose_name_plural = "descripciones de planetas"

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions')

