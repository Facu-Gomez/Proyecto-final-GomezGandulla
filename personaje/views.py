from django.shortcuts import redirect, render
from . import models, forms
from django.db.models import Q
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound

def home(request):
    return render(request, "personaje/index.html")

class PersonajeList(ListView):
    model = models.Personaje
    template_name = 'personaje/personaje_list.html' 
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(nombre__icontains=consulta) |  
                Q(apellido__icontains=consulta)  
            )

        return queryset
    
class PersonajeDetail(DetailView):
    model = models.Personaje
    context_object_name= "personaje"

class PersonajeDelete(DeleteView):
    model = models.Personaje
    template_name = "personaje/personaje_delete.html"
    success_url = reverse_lazy("personaje:personaje_list")

class PersonajeUpdate(UpdateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("personaje:personaje_list")

class PersonajeCreate(CreateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("personaje:home")

 

def personaje_create(request):
    if request.method == "POST":
        form = forms.PersonajeForm(request.POST)
        if form.is_valid():
            planeta_origen = form.cleaned_data.get('planeta_origen_id')

            if planeta_origen:
                form.save()
                return redirect("personaje:home")
            else:
                # Proporciona un mensaje de error al usuario si el planeta no existe
                return HttpResponseNotFound("El planeta seleccionado no existe.")
    else:
        form = forms.PersonajeForm()
    return render(request, "personaje/personaje_create.html", {"form": form})


