from django import forms
from . import models

#class ProductoCategoriaForm(forms.Form):
#    name = forms.CharField()
#    description = forms.CharField()

class NavesForm(forms.ModelForm):
    class Meta:
        model = models.Nave
        fields = "__all__"
