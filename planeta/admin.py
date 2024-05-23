from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Planetas"

class PlanetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre",) #la coma al final sirve para tomar la variable como una tupla

admin.site.register(models.Planeta, PlanetaAdmin)
