from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import InputMasterSupplier, InputMasterPelanggan, InputMasterBarang

from .models import MasterSupplier, MasterPelanggan, MasterBarang

from django.contrib.auth.models import User
from django.contrib import auth

from django.db.models import Q

import datetime

# Create your views here.
def indeks(request):
    loginkan=0
    
    if request.method == 'POST':
        loginkan=1
        username=request.POST['txtusername']
        password=request.POST['txtpassword']
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
    return render(request, 'coba.html',{'loginkan':loginkan})

def Input_Master_Supplier(request):
    errornya = None
    apa_post= False
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            apa_post=True
            forms = InputMasterSupplier(request.POST)
            if(forms.is_valid()):
                forms.save()
            else:
                errornya =forms.errors.items()

        forms = InputMasterSupplier()
        return render(request, 'master/input-master-supplier.html',{'form':forms,'errornya':errornya,'apa_post':apa_post})

def Delete_Master_Supplier(request,idsupplier):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        MasterSupplier.objects.get(kode_supplier=idsupplier).delete()
        return HttpResponseRedirect('/i/ms/')

def Input_Master_Pelanggan(request):
    errornya = None
    apa_post= False
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            apa_post=True
            forms = InputMasterPelanggan(request.POST,request.FILES)
            if(forms.is_valid()):
                forms.save()
            else:
                errornya = forms.errors.items()

        forms = InputMasterPelanggan()
        return render(request, 'master/input-master_pelanggan.html',{'form':forms,'errornya':errornya,'apa_post':apa_post})

def Initial_Input_Master(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'master/initial_input_masterdata.html')

def Pos(request,nomor):
    mydate = datetime.date.today()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,'POS/initial.html',{'nomor':nomor,'mydate':mydate})

def chartku(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        labelx = [50,60,70,80,90,100,110,120,130,140,150]
        labely = [7,8,8,9,9,9,10,11,14,14,15]
        return render(request,'POS/graph.html',{'labelx':labelx,'labely':labely})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def Input_Master_Barang(request):
    errornya = None
    apa_post= False
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            apa_post=True
            forms = InputMasterBarang(request.POST,request.FILES)
            if forms.is_valid():
                forms.save()
            else:
                errornya= forms.errors.items()
                
        forms = InputMasterBarang()
        return render(request,"master/input_master_barang.html",{'form':forms,'errornya':errornya,'apa_post':apa_post})

def Delete_Master_Barang(request,idbarang):
    MasterBarang.objects.get(id_barang=idbarang).delete()
    return HttpResponseRedirect('/v/b/')

def Initial_View_Master(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,"master/initial_view_master_data.html")

def View_Master_Pelanggan(request):
    data = MasterPelanggan.objects.all()
    jml_data = data.count()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,"master/view_master_data_pelanggan.html",{'data':data,'jml_data':jml_data})

def View_Master_Barang(request):
    data = MasterBarang.objects.all()
    jml_data = data.count()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,"master/view_master_data_barang.html",{'data':data,'jml_data':jml_data})

def View_Master_Supplier(request):
    data = MasterSupplier.objects.all()
    jml_data = data.count()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,"master/view_master_data_supplier.html",{'data':data,'jml_data':jml_data})

def Find_kode_barang(request):
    data = MasterBarang.objects.all()
    data_supplier = MasterSupplier.objects.all()
    data_pelanggan = MasterPelanggan.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            filter_data = request.POST['txtcari']
            data = data.filter(Q(id_barang__contains=filter_data) | Q(nama_barang__contains=filter_data))
            data_supplier = data_supplier.filter(Q(alamat__contains=filter_data) |Q(kode_supplier__contains=filter_data) | Q(nama_supplier__contains=filter_data))
            data_pelanggan = data_pelanggan.filter(Q(alamat_pelanggan__contains=filter_data) | Q(kode_pelanggan__contains=filter_data) | Q(nama_pelanggan__contains=filter_data))

            if data.exists():
                if filter_data=="":
                    filter_data = "semua"
                jumlah_data = data.count()
            else:
                jumlah_data = 0

            if data_supplier.exists():
                jumlah_data_supplier = data_supplier.count()
            else:
                jumlah_data_supplier = 0
            
            if data_pelanggan.exists():
                jumlah_data_pelanggan = data_pelanggan.count()
            else:
                jumlah_data_pelanggan = 0
            
                
        else:
            filter_data = "semua"
            jumlah_data = data.count()
            jumlah_data_supplier = data_supplier.count()
            jumlah_data_pelanggan = data_pelanggan.count()
        return render(request,'search_barang.html',{'data':data,'filter_data':filter_data,'jumlah_data':jumlah_data,'jumlah_data_supplier':jumlah_data_supplier,'jumlah_data_pelanggan':jumlah_data_pelanggan,'data_pelanggan':data_pelanggan,'data_supplier':data_supplier})