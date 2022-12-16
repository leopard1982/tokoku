from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.indeks, name="indeks"),
    path("i/ms/", views.Input_Master_Supplier,name="Input_Master_Supplier"),
    path("d/ms/<str:idsupplier>", views.Delete_Master_Supplier,name="Delete_Master_Supplier"),
    path("d/mb/<str:idbarang>", views.Delete_Master_Barang,name="Delete_Master_Barang"),
    path("d/ms/<str:idsupplier>", views.Delete_Master_Supplier,name="Delete_Master_Supplier"),
    path("d/mp/<str:idpelanggan>", views.Delete_Master_Pelanggan,name="Delete_Master_Pelanggan"),
    path("i/mp/", views.Input_Master_Pelanggan,name="Input_Master_Pelanggan"),
    path("i/mb/", views.Input_Master_Barang,name="Input_Master_Barang"),
    path("i/", views.Initial_Input_Master,name="Initial_Input_Master"),
    path('POS/<str:nomor>/',views.Pos,name="Pos"),
    path('POS/<str:nomor>/<str:id_barang>/d/',views.Pos_delete,name="Pos_delete"),
    path('POS-grosir/<str:nomor>/',views.Pos_grosir,name="Pos_grosir"),
    path('chart/',views.chartku,name='chartku'),
    path('logout/',views.logout,name='logout'),
    path('v/',views.Initial_View_Master,name='Initial_View_Master'),
    path('v/p/',views.View_Master_Pelanggan,name='View_Master_Pelanggan'),
    path('v/b/',views.View_Master_Barang,name='View_Master_Barang'),
    path('v/s/',views.View_Master_Supplier,name='View_Master_Supplier'),
    path('f/',views.Find_kode_barang,name='Find_kode_barang'),
    path('nota_ecer/<str:nomor>/',views.Cetak_Nota_Ecer,name="Cetak_Nota_Ecer"),
    path('h/',views.history_penjualan, name="history_penjualan"),
    path('u/',views.untungku,name='untungku'),
]
