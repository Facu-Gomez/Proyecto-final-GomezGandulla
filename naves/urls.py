from django.urls import path

from . import views

app_name = "naves"

urlpatterns = [
    path("", views.home, name="home"),
    path("naves/create/", views.NavesCreate.as_view(), name="naves_create"),
    path("naves/list/", views.NavesList.as_view(), name="naves_list"),
    path("naves/detail/<int:pk>", views.NavesDetail.as_view(), name="naves_detail"),
    path("naves/update/<int:pk>", views.NavesUpdate.as_view(), name="naves_update"),
    path("naves/delete/<int:pk>", views.NavesDelete.as_view(), name="naves_delete")
]

