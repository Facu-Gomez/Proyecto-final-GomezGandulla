from django.urls import path

from . import views

app_name = "planeta"


urlpatterns = [
    path("", views.home, name="home"),
    path("planeta/create/", views.PlanetaCreate.as_view(), name="planeta_create"),
    #path("planeta/list/", views.planeta_list, name="planeta_list"),
    path("planeta/list/", views.PlanetaList.as_view(), name="planeta_list"),
    path("planeta/detail/<int:pk>", views.PlanetaDetail.as_view(), name="planeta_detail"),
    path("planeta/update/<int:pk>", views.PlanetaUpdate.as_view(), name="planeta_update"),
    path("planeta/delete/<int:pk>", views.PlanetaDelete.as_view(), name="planeta_delete")
]
    