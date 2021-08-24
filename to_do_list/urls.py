from django.urls import path
from . import views

urlpatterns = [
    path("",views.to_do,name="home"),
    path("list/",views.to_do_list,name="list"),
    path("update/<int:id>/",views.to_do_update,name="update"),
    path("list/<int:id>/",views.to_do_delete,name="delete"),
]
