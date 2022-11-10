
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.indeks, name="indeks"),
    path("i/ms/", views.Input_Master_Supplier,name="Input_Master_Supplier"),
    path("i/mp/", views.Input_Master_Pelanggan,name="Input_Master_Pelanggan"),
    path("i/", views.Initial_Input_Master,name="Initial_Input_Master"),
]
