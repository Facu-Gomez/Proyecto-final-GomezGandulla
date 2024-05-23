# urls.py
from django.urls import path
from . import views

app_name = "personaje"

urlpatterns = [
    path("", views.home, name="home"),
    path("personaje/create/", views.PersonajeCreate.as_view(), name="personaje_create"),
    path("personaje/list/", views.PersonajeList.as_view(), name="personaje_list"),
    path("personaje/detail/<int:pk>", views.PersonajeDetail.as_view(), name="personaje_detail"),
    path("personaje/update/<int:pk>", views.PersonajeUpdate.as_view(), name="personaje_update"),
    path("personaje/delete/<int:pk>", views.PersonajeDelete.as_view(), name="personaje_delete"),
]
