from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path("",views.index,name = "home"),
    path("details",views.details,name = "details"),
    path("delete/<int:id>",views.delete,name = "delete"),
    path("update/<int:id>",views.update,name = "update"),
    path("editrecord/<int:id>",views.editrecord,name = "detailsnew"),

]