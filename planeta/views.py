from django.shortcuts import redirect, render
from . import models, forms
from django.db.models import Q
from .models import Planeta
from django.views.generic import (ListView, DetailView, DeleteView, CreateView, UpdateView)
from django.urls import reverse_lazy

def home(request):
    return render(request, "planeta/index.html")

#def planeta_list(request):
#        if "consulta" in request.GET:  
#            consulta = request.GET["consulta"]
#            planetas = Planeta.objects.filter(nombre__icontains=consulta)
#        else:        
#            planetas = Planeta.objects.all()
#            context = {"planetas": planetas}  
#            return render(request, "planeta/planeta_list.html", context)

#def planeta_create(request):
#    if request.method == "POST":
#        form = forms.PlanetaForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("planeta:home")
#    else: #request.method == "GET"
#        form = forms.PlanetaForm()
#    return render(request, "planeta/planeta_create.html", {"form": form})

#def planeta_update(request, pk: int):
#    query = models.Planeta.objects.get(id=pk)
#    if request.method == "POST":
#        form = forms.PlanetaForm(request.POST, instance=query)
#        if form.is_valid():
#            form.save()
#            return redirect("planeta:planeta_list")
#    else: 
#        form = forms.PlanetaForm(instance=query)
#    return render(request, "planeta/planeta_update.html", {"form": form})

#def planeta_detail(request, pk):
#     query = models.Planeta.objects.get(id=pk)
#     return render(request, "planeta/planeta_detail.html", {"planeta": query})

#def planeta_delete(request, pk: int):
#    query = models.Planeta.objects.get(id=pk)
#    if request.method == "POST":
#        query.delete()
#        return redirect("planeta:planeta_list")
#    return render(request, "planeta/planeta_delete.html", context={"planeta": query})

class PlanetaList(ListView):
    model = models.Planeta
    template_name = 'planeta/planeta_list.html' 
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')  

        if consulta:  
            queryset = queryset.filter(
                Q(nombre__icontains=consulta) |  
                Q(descripcion__icontains=consulta)  
            )

        return queryset

class PlanetaDetail(DetailView):
    model = models.Planeta
    context_object_name= "planeta"

class PlanetaDelete(DeleteView):
    model = models.Planeta
    template_name = "planeta/planeta_delete.html"
    success_url = reverse_lazy("planeta:planeta_list")
    
class PlanetaCreate(CreateView):
    model = models.Planeta
    form_class = forms.PlanetaForm
    success_url = reverse_lazy("planeta:home")

class PlanetaUpdate(UpdateView):
    model = models.Planeta
    form_class = forms.PlanetaForm
    success_url = reverse_lazy("planeta:planeta_list")