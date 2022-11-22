from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import InputMasterSupplier, InputMasterPelanggan, InputMasterBarang

from .models import MasterSupplier, MasterPelanggan

from django.contrib.auth.models import User
from django.contrib import auth

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
        return render(request, 'input-master-supplier.html',{'form':forms,'errornya':errornya,'apa_post':apa_post})

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
        return render(request, 'input-master_pelanggan.html',{'form':forms,'errornya':errornya,'apa_post':apa_post})

def Initial_Input_Master(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'initial_masterdata.html')

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
    if request.method == "POST":
        apa_post=True
        forms = InputMasterBarang(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
        else:
            errornya= forms.errors.items()
            
    forms = InputMasterBarang()
    return render(request,"input_master_barang.html",{'form':forms,'errornya':errornya,'apa_post':apa_post})