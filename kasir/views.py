from django.shortcuts import render, HttpResponse

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