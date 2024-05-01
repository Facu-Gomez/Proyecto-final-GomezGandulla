from django import forms
from . import models

#class ProductoCategoriaForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField()

class PlanetaForm(forms.ModelForm):
    class Meta:
        model = models.Planeta
        fields = "__all__"
