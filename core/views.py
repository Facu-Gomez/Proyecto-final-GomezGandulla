from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy


def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/aboutme.html")


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"

    def get_success_url(self):
        return reverse_lazy('core:home')
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('core:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado exitosamente.")
            return redirect('core:home')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'core/edit_profile.html', {'form': form})