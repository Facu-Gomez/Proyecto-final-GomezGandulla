from django import forms
from . import models
from .models import Personaje, Planeta

class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PersonajeForm, self).__init__(*args, **kwargs)
        queryset = models.Planeta.objects.all()
        if queryset.exists():
            self.fields['planeta_origen_id'].queryset = queryset
        else:

            self.fields['planeta_origen_id'].widget.attrs['disabled'] = True
            self.fields['planeta_origen_id'].widget.attrs['placeholder'] = 'No hay planetas disponibles'
