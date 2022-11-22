from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.indeks, name="indeks"),
    path("i/ms/", views.Input_Master_Supplier,name="Input_Master_Supplier"),
    path("d/ms/<str:idsupplier>", views.Delete_Master_Supplier,name="Delete_Master_Supplier"),
    path("i/mp/", views.Input_Master_Pelanggan,name="Input_Master_Pelanggan"),
    path("i/mb/", views.Input_Master_Barang,name="Input_Master_Barang"),
    path("i/", views.Initial_Input_Master,name="Initial_Input_Master"),
    path('POS/<str:nomor>/',views.Pos,name="Pos"),
    path('chart/',views.chartku,name='chartku'),
    path('logout/',views.logout,name='logout'),
    path('v/',views.Initial_View_Master,name='Initial_View_Master'),
    path('v/p/',views.View_Master_Pelanggan,name='View_Master_Pelanggan'),
]
