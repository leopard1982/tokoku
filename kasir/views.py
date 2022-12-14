from django.shortcuts import render, HttpResponse, HttpResponseRedirect

from .forms import InputMasterSupplier, InputMasterPelanggan, InputMasterBarang

from .models import MasterSupplier, MasterPelanggan, MasterBarang, MasterParameter

from .models import POS1_ecer, POS2_ecer, POS3_ecer
from .models import POS1_grosir, POS2_grosir, POS3_grosir, Posting

from django.contrib.auth.models import User
from django.contrib import auth

from django.db.models import Q
from django.db.models import F
from django.db.models import Sum

import datetime

# Create your views here.
def indeks(request):
    loginkan=0
    id_sistemnya=""

    if request.method == 'POST':
        loginkan=1
        username=request.POST['txtusername']
        password=request.POST['txtpassword']
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)

    param = MasterParameter.objects.all()
    if param.count() == 0:
        param = MasterParameter()
        param.id_sistem="LT001"
        param.counter_nota=1
        param.counter1_ecer=0
        param.counter2_ecer=0
        param.counter3_ecer=0
        param.counter1_grosir=0
        param.counter1_grosir=0
        param.counter1_grosir=0
        param.save()

    param = MasterParameter.objects.all()

    #jika eceran belum ada
    eceranku = MasterPelanggan.objects.all().filter(kode_pelanggan="Eceran")
    if not eceranku.exists():
        eceranku = MasterPelanggan()
        eceranku.kode_pelanggan = "Eceran"
        eceranku.nama_pelanggan = "Eceran"
        eceranku.nomor_tlp = "sekian sekian"
        eceranku.alamat_pelanggan = "mana mana"
        eceranku.tipe = "E"
        eceranku.hapus = True
        eceranku.save()

    for par in param:
        id_sistemnya = par.id_sistem
    return render(request, 'coba.html',{'loginkan':loginkan,'id_sistem':id_sistemnya})

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
    nomor_notanya =0
    belanjaku=None
    total_item = 0
    total_belanja =0

    if(nomor=="1"):
        belanjaku = POS1_ecer.objects.all().filter(userid=request.user.id)
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter1_ecer
    elif(nomor=="2"):
        belanjaku = POS2_ecer.objects.all().filter(userid=request.user.id)
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter2_ecer
    elif(nomor=="3"):
        belanjaku = POS3_ecer.objects.all().filter(userid=request.user.id)
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter3_ecer

    if request.method == "POST":    
        '''simpan transaksi'''
        '''cek ini pos1, 2 atau 3'''
        datastream = request.POST['datastream']
        '''cek id sistem'''
        id_sistem = ""
        '''jika isi pos1, atau 2 atau 3 kosong maka counter akan nambah 1'''
        pos_ke = int(datastream.split('^')[0])
        
        if(pos_ke==1):
            if(POS1_ecer.objects.all().filter(userid=request.user.id).count()==0):
                MasterParameter.objects.update(counter_nota=F('counter_nota')+1)
                MasterParameter.objects.update(counter1_ecer = F('counter_nota')-1)
                '''ITS COOL WORK'''
            for param in MasterParameter.objects.all():
                nomor_notanya = param.counter1_ecer
                id_sistem = param.id_sistem
            '''cek apakah sudah pernah diinput'''
            hai_pos1 = POS1_ecer.objects.all().filter(id_barang=datastream.split('^')[2]).filter(userid=request.user.id)
            if hai_pos1.exists():
                POS1_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(jumlah_barang=F('jumlah_barang')+int( datastream.split('^')[7]))
                POS1_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(sub_total=F('jumlah_barang')*F('harga_barang'))
                POS1_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(rupiah_discount=F('sub_total')*F('discount')/100)
                POS1_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(total=F('sub_total')-F('rupiah_discount'))
            else:
                pos1_ecer = POS1_ecer()
                pos1_ecer.userid = User.objects.get(id=request.user.id)
                pos1_ecer.kode_sistem = id_sistem
                pos1_ecer.kode_pelanggan = MasterPelanggan.objects.get(kode_pelanggan="Eceran")
                pos1_ecer.nomor_nota = nomor_notanya
                pos1_ecer.id_barang = MasterBarang.objects.get(id_barang=datastream.split('^')[2])
                pos1_ecer.harga_barang = int(datastream.split('^')[6])
                pos1_ecer.jumlah_barang = datastream.split('^')[7]
                pos1_ecer.discount = datastream.split('^')[8]
                pos1_ecer.rupiah_discount = datastream.split('^')[9]
                pos1_ecer.sub_total = int(datastream.split('^')[6])*int(datastream.split('^')[7])
                pos1_ecer.total = int(datastream.split('^')[6])*int(datastream.split('^')[7]) - int(datastream.split('^')[9])
                pos1_ecer.posting=False
                pos1_ecer.save()
            belanjaku = POS1_ecer.objects.all().filter(userid=request.user.id)
            total_item = POS1_ecer.objects.all().filter(userid=request.user.id).count()
            
        elif pos_ke==2:
            if(POS2_ecer.objects.all().filter(userid=request.user.id).count()==0):
                MasterParameter.objects.update(counter_nota=F('counter_nota')+1)
                MasterParameter.objects.update(counter2_ecer = F('counter_nota')-1)
                '''ITS COOL WORK'''
            for param in MasterParameter.objects.all():
                nomor_notanya = param.counter2_ecer
                id_sistem = param.id_sistem
            '''cek apakah sudah pernah diinput'''
            hai_pos2 = POS2_ecer.objects.all().filter(id_barang=datastream.split('^')[2]).filter(userid=request.user.id)
            if hai_pos2.exists():
                POS2_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(jumlah_barang=F('jumlah_barang')+int( datastream.split('^')[7]))
                POS2_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(sub_total=F('jumlah_barang')*F('harga_barang'))
                POS2_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(rupiah_discount=F('sub_total')*F('discount')/100)
                POS2_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(total=F('sub_total')-F('rupiah_discount'))
            else:
                pos2_ecer = POS2_ecer()
                pos2_ecer.userid =User.objects.get(id=request.user.id)
                pos2_ecer.kode_sistem = id_sistem
                pos2_ecer.kode_pelanggan =  MasterPelanggan.objects.get(kode_pelanggan="Eceran")
                pos2_ecer.nomor_nota = nomor_notanya
                pos2_ecer.id_barang = MasterBarang.objects.get(id_barang=datastream.split('^')[2])
                pos2_ecer.harga_barang = int(datastream.split('^')[6])
                pos2_ecer.nama_barang = datastream.split('^')[3]
                pos2_ecer.harga_barang = datastream.split('^')[6]
                pos2_ecer.jumlah_barang = datastream.split('^')[7]
                pos2_ecer.discount = datastream.split('^')[8]
                pos2_ecer.rupiah_discount = datastream.split('^')[9]
                pos2_ecer.sub_total = int(datastream.split('^')[6])*int(datastream.split('^')[7])
                pos2_ecer.total = int(datastream.split('^')[6])*int(datastream.split('^')[7]) - int(datastream.split('^')[9])
                pos2_ecer.posting=False
                pos2_ecer.save()
            belanjaku = POS2_ecer.objects.all().filter(userid=request.user.id)
            total_item = POS2_ecer.objects.all().filter(userid=request.user.id).count()
            
        elif pos_ke==3:
            if(POS3_ecer.objects.all().filter(userid=request.user.id).count()==0):
                MasterParameter.objects.update(counter_nota=F('counter_nota')+1)
                MasterParameter.objects.update(counter3_ecer = F('counter_nota')-1)
                '''ITS COOL WORK'''
            for param in MasterParameter.objects.all():
                nomor_notanya = param.counter3_ecer
                id_sistem = param.id_sistem
            '''cek apakah sudah pernah diinput'''
            hai_pos3 = POS3_ecer.objects.all().filter(id_barang=datastream.split('^')[2]).filter(userid=request.user.id)
            if hai_pos3.exists():
                POS3_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(jumlah_barang=F('jumlah_barang')+int( datastream.split('^')[7]))
                POS3_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(sub_total=F('jumlah_barang')*F('harga_barang'))
                POS3_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(rupiah_discount=F('sub_total')*F('discount')/100)
                POS3_ecer.objects.filter(id_barang=datastream.split('^')[2]).update(total=F('sub_total')-F('rupiah_discount'))
            else:
                pos3_ecer = POS3_ecer()
                pos3_ecer.userid = User.objects.get(id=request.user.id)
                pos3_ecer.kode_sistem = id_sistem
                pos3_ecer.kode_pelanggan = MasterPelanggan.objects.get(kode_pelanggan="Eceran")
                pos3_ecer.nomor_nota = nomor_notanya
                pos3_ecer.id_barang = MasterBarang.objects.get(id_barang=datastream.split('^')[2])
                pos3_ecer.harga_barang = int(datastream.split('^')[6]) 
                pos3_ecer.nama_barang = datastream.split('^')[3]
                pos3_ecer.harga_barang = datastream.split('^')[6]
                pos3_ecer.jumlah_barang = datastream.split('^')[7]
                pos3_ecer.discount = datastream.split('^')[8]
                pos3_ecer.rupiah_discount = datastream.split('^')[9]
                pos3_ecer.sub_total = int(datastream.split('^')[6])*int(datastream.split('^')[7])
                pos3_ecer.total = int(datastream.split('^')[6])*int(datastream.split('^')[7]) - int(datastream.split('^')[9])
                pos3_ecer.posting=False
                pos3_ecer.save()
            belanjaku = POS3_ecer.objects.all().filter(userid=request.user.id)
            total_item = POS2_ecer.objects.all().filter(userid=request.user.id).count()

    mydate = datetime.date.today()
    daftarbarang = MasterBarang.objects.all()

    if(nomor=="1"):
        total_item = POS1_ecer.objects.all().filter(userid=request.user.id).count()
        total_belanja = POS1_ecer.objects.filter(userid=request.user.id).aggregate(jumlah=Sum('total'))
        total_belanja = total_belanja['jumlah']
    elif(nomor=="2"):
        total_item = POS2_ecer.objects.all().filter(userid=request.user.id).count()
        total_belanja = POS2_ecer.objects.filter(userid=request.user.id).aggregate(jumlah=Sum('total'))
        total_belanja = total_belanja['jumlah']
    elif(nomor=="3"):
        total_item = POS3_ecer.objects.all().filter(userid=request.user.id).count()
        total_belanja = POS3_ecer.objects.filter(userid=request.user.id).aggregate(jumlah=Sum('total'))
        total_belanja = total_belanja['jumlah']


    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,'POS/initial.html',{'nomor':nomor,'mydate':mydate,'daftarbarang':daftarbarang,'belanjaku':belanjaku,'nomornota':nomor_notanya,'totalitem':total_item,'totalbelanja':total_belanja})

def Cetak_Nota_Ecer(request,nomor):
    nomor_pos = int(nomor)
    
    tanggal_jam = datetime.datetime.now()
    nomor_notanya =0
    belanjaku=""
    total_belanja =0
    mydate = datetime.date.today()
    
    if nomor_pos == 1:
        belanjaku = POS1_ecer.objects.all().filter(userid=request.user.id)
        total_item = belanjaku.count()
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter1_ecer
    elif nomor_pos == 2:
        belanjaku = POS2_ecer.objects.all().filter(userid=request.user.id)
        total_item = belanjaku.count()
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter2_ecer
    elif nomor_pos == 3:
        belanjaku = POS2_ecer.objects.all().filter(userid=request.user.id)
        total_item = belanjaku.count()
        for param in MasterParameter.objects.all():
            nomor_notanya = param.counter3_ecer


    total_belanja = POS1_ecer.objects.aggregate(jumlah=Sum('total'))
    total_belanja = total_belanja['jumlah']

    '''posting data'''
    for belanja in belanjaku:
        posting = Posting()
        posting.userid = User.objects.get(id=request.user.id)
        posting.kode_sistem  = MasterParameter.objects.get()
        posting.id_barang = MasterBarang.objects.get(id_barang = belanja.id_barang)
        posting.kode_pelanggan = MasterPelanggan.objects.get(kode_pelanggan=belanja.kode_pelanggan.kode_pelanggan)
        posting.save()
    
    '''hapus data pos1 atau 2 atau 3'''
    if nomor_pos == 1:
        POS1_ecer.objects.all().filter(userid=request.user.id).delete()
    elif nomor_pos == 2:
        POS2_ecer.objects.all().filter(userid=request.user.id).delete()
    elif nomor_pos == 3:
        POS3_ecer.objects.all().filter(userid=request.user.id).delete()
        

    return render(request,'POS/nota_ecer.html',{'mydate':mydate,'belanjaku':belanjaku,'nomornota':nomor_notanya,'totalitem':total_item,'totalbelanja':total_belanja,'tanggaljam':tanggal_jam})

def Pos_delete(request,nomor,id_barang):
    if nomor =="1" :
        print(id_barang)
        POS1_ecer.objects.filter(id_barang=id_barang).filter(userid=request.user.id).delete()
    elif nomor == "2":
        POS2_ecer.objects.filter(id_barang=id_barang).filter(userid=request.user.id).delete()
    elif nomor == "3":
        POS3_ecer.objects.filter(id_barang=id_barang).filter(userid=request.user.id).delete()
    return HttpResponseRedirect('/POS/' + str(nomor) + '/')

def Pos_grosir(request,nomor):
    mydate = datetime.date.today()
    daftarbarang = MasterBarang.objects.all()
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request,'POS/initial_grosir.html',{'nomor':nomor,'mydate':mydate,'daftarbarang':daftarbarang})


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
                MasterBarang.objects.update(stok_akhir=F('stok_awal'))
            else:
                errornya= forms.errors.items()
                
        forms = InputMasterBarang()
        return render(request,"master/input_master_barang.html",{'form':forms,'errornya':errornya,'apa_post':apa_post})

def Delete_Master_Barang(request,idbarang):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        try:
            MasterBarang.objects.get(id_barang=idbarang).delete()
        except:
            pass
        return HttpResponseRedirect('/v/b/')

def Delete_Master_Supplier(request,idsupplier):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        try:
            MasterSupplier.objects.get(kode_supplier=idsupplier).delete()
        except:
            pass
        return HttpResponseRedirect('/v/s/')

def Delete_Master_Pelanggan(request,idpelanggan):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        try:
            MasterPelanggan.objects.get(kode_pelanggan=idpelanggan).delete()
        except:
            pass
        return HttpResponseRedirect('/v/p/')

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

def history_penjualan(request):
    history = list(Posting.objects.all())

    return render(request,'POS/history.html',{'history':history})