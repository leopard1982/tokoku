from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import InputMasterSupplier, InputMasterPelanggan

from .models import MasterSupplier, MasterPelanggan

# Create your views here.
def indeks(request):
    return render(request, 'coba.html')

def Input_Master_Supplier(request):
    if request.method == "POST":
        forms = InputMasterSupplier(request.POST)
        if(forms.is_valid()):
            forms.save()
        else:
            print(forms)

    forms = InputMasterSupplier()
    data = MasterSupplier.objects.all()
    return render(request, 'input-master-supplier.html',{'form':forms,'data':data})

def Delete_Master_Supplier(request,idsupplier):
    MasterSupplier.objects.get(kode_supplier=idsupplier).delete()
    return HttpResponseRedirect('/i/ms/')

def Input_Master_Pelanggan(request):
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
    return render(request, 'initial_masterdata.html')

def Pos(request):
    return render(request,'POS/initial.html')

def chartku(request):
    labelx = [50,60,70,80,90,100,110,120,130,140,150]
    labely = [7,8,8,9,9,9,10,11,14,14,15]
    return render(request,'POS/graph.html',{'labelx':labelx,'labely':labely})