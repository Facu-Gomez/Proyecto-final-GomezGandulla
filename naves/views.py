from django.shortcuts import redirect, render
from . import models, forms
from django.db.models import Q
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.urls import reverse_lazy

def home(request):
    return render(request, "naves/index.html")

class NavesList(ListView):
    model = models.Nave
    template_name = "naves/naves_list.html"
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(nombre__icontains=consulta) |  
                Q(descripcion__icontains=consulta)  
            )

        return queryset
    

class NavesDetail(DetailView):
    model = models.Nave
    context_object_name= "naves"
    template_name = "naves/naves_detail.html"

class NavesDelete(DeleteView):
    model = models.Nave
    template_name = "naves/naves_delete.html"
    success_url = reverse_lazy("naves:naves_list")
    
class NavesCreate(CreateView):
    model = models.Nave
    form_class = forms.NavesForm
    success_url = reverse_lazy("naves:home")
    template_name = "naves/naves_form.html"

class NavesUpdate(UpdateView):
    model = models.Nave
    form_class = forms.NavesForm
    success_url = reverse_lazy("naves:home")
    template_name = "naves/naves_form.html"