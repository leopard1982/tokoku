from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import InputMasterSupplier, InputMasterPelanggan

from .models import MasterSupplier, MasterPelanggan

from django.contrib.auth.models import User
from django.contrib import auth

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
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            forms = InputMasterSupplier(request.POST)
            if(forms.is_valid()):
                forms.save()

        forms = InputMasterSupplier()
        data = MasterSupplier.objects.all()
        return render(request, 'input-master-supplier.html',{'form':forms,'data':data})

def Delete_Master_Supplier(request,idsupplier):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        MasterSupplier.objects.get(kode_supplier=idsupplier).delete()
        return HttpResponseRedirect('/i/ms/')

def Input_Master_Pelanggan(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            forms = InputMasterPelanggan(request.POST,request.FILES)
            if(forms.is_valid()):
                forms.save()
            else:
                print(forms)

        forms = InputMasterPelanggan()
        data = MasterPelanggan.objects.all()
        return render(request, 'input-master_pelanggan.html',{'form':forms,'data':data})

def Initial_Input_Master(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'initial_masterdata.html')

def Pos(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,'POS/initial.html')

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