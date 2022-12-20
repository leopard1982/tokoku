from django.db import models

from django.urls import reverse

from django.contrib.auth.models import User


class MasterParameter(models.Model):
	id_sistem = models.CharField(max_length=6,default="-",primary_key=True,blank=False,null=False)
	counter_nota = models.PositiveBigIntegerField(default=0)
	counter1_ecer = models.PositiveBigIntegerField(default=0)
	counter2_ecer = models.PositiveBigIntegerField(default=0)
	counter3_ecer = models.PositiveBigIntegerField(default=0)
	counter1_grosir = models.PositiveBigIntegerField(default=0)
	counter2_grosir = models.PositiveBigIntegerField(default=0)
	counter3_grosir = models.PositiveBigIntegerField(default=0)


# Create your models here.
class MasterSupplier(models.Model):
	kode_supplier= models.CharField(max_length=100,verbose_name="Kode Supplier",default="",primary_key=True,null=False,blank=False)
	nama_supplier = models.CharField(max_length=200,verbose_name="Nama Supplier",default="",null=False,blank=False)
	tlp1 = models.CharField(max_length=15,verbose_name="No. Telpon #1",default="",null=False,blank=False)
	tlp2 = models.CharField(max_length=15,verbose_name="No. Telpon #2",default="",null=True,blank=True)
	alamat = models.CharField(max_length=200,verbose_name="Alamat Supplier",default="",null=False,blank=False)
	hutang_awal =models.PositiveIntegerField(verbose_name="Hutang Awal",default=0)
	hutang_tambahan=models.PositiveIntegerField(verbose_name="Hutang Tambahan",default=0)
	hutang_akhir = models.PositiveIntegerField(verbose_name="Hutang Akhir",default=0)
	catatan = models.CharField(max_length=200,verbose_name="Catatan",default="-")
	hapus= models.BooleanField(default=True)

	def __str__(self):
		return "%s "%(self.nama_supplier)


	def delete_master(self):
		return reverse('Delete_Master_Supplier',args=[str(self.kode_supplier)])

	class Meta:
		unique_together=["kode_supplier","nama_supplier"]
		ordering = ["kode_supplier","nama_supplier"]

class MasterPelanggan(models.Model):
	pilihan = [('A','Pelanggan Harga#1'),('B','Pelanggan Harga#2'),('C','Pelanggan Harga#3'),('E','Pelanggan Eceran')
	]
	kode_pelanggan = models.CharField(max_length=100,verbose_name="Kode Pelanggan",null=False,blank=False,primary_key=True)
	nama_pelanggan = models.CharField(max_length=100,verbose_name="Nama Pelanggan",null=False,blank=False)
	nomor_tlp = models.CharField(max_length=15,verbose_name="Nomor Telepon",null=False,blank=False)
	alamat_pelanggan = models.CharField(max_length=100,verbose_name="Alamat KTP",null=False,blank=False)
	foto_ktp = models.ImageField(verbose_name="Foto KTP",upload_to="ktp",null=True,blank=True)
	tipe = models.CharField(max_length=1,choices=pilihan,verbose_name="Tipe Pelanggan",null=False,blank=False)
	hapus= models.BooleanField(default=True)
	
	def __str_(self):
		return "%s"%(self.nama_pelanggan)

	class Meta:
		ordering = ['kode_pelanggan','nama_pelanggan']

class MasterBarang(models.Model):
	pilih_satuan = [('D','Kardus'),
		('R','Renceng'),
		('E','Ecer')]
	id_barang = models.CharField(max_length=100,verbose_name="ID Barang",null=False,blank=False,primary_key=True,default="-")
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")
	stok_awal = models.PositiveBigIntegerField(verbose_name="Stok Awal Barang",default=0,null=False,blank=False)
	stok_beli = models.PositiveBigIntegerField(verbose_name="Stok Pembelian",default=0,null=False,blank=False)
	stok_rusak = models.PositiveBigIntegerField(verbose_name="Stok Barang Rusak",default=0,null=False,blank=False)
	stok_akhir = models.PositiveBigIntegerField(verbose_name="Stok Barang Akhir",default=0,null=False,blank=False)
	harga_modal = models.PositiveBigIntegerField(verbose_name="Harga Modal",default=0,null=False,blank=False)
	harga_ecer = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	harga_grosir1 = models.PositiveBigIntegerField(verbose_name="Harga Grosir#1",default=0,null=False,blank=False)
	harga_grosir2 = models.PositiveBigIntegerField(verbose_name="Harga Grosir#2",default=0,null=False,blank=False)
	harga_grosir3 = models.PositiveBigIntegerField(verbose_name="Harga Grosir#3",default=0,null=False,blank=False)
	satuan_barang = models.CharField(verbose_name="Satuan Barang",max_length=1,choices=pilih_satuan,null=False,blank=False,default="D")
	keterangan_isi = models.CharField(verbose_name="Keterangan Isi",max_length=100,null=False,blank=False)
	foto = models.ImageField(verbose_name="Foto Barang",upload_to="stok_barang",null=False,blank=False)
	hapus= models.BooleanField(default=True)
	discount = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return "%s"%(self.nama_barang)
	
	class Meta:
		ordering = ['id_barang','nama_barang']
	
class POS1_ecer(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class POS2_ecer(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class POS3_ecer(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class POS1_grosir(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class POS2_grosir(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class POS3_grosir(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")	
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)	
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	posting=models.BooleanField(default=False)

class Posting(models.Model):
	kode_sistem = models.CharField(max_length=100,default="-",null=False,blank=False)
	userid = models.ForeignKey(User,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	kode_pelanggan = models.ForeignKey(MasterPelanggan,models.RESTRICT)
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,null=False,blank=False,default="0",on_delete=models.RESTRICT)
	nama_barang = models.CharField(max_length=100,verbose_name="Nama Barang",null=False,blank=False,default="-")	
	harga_modal = models.PositiveIntegerField(default=0)
	harga_barang = models.PositiveBigIntegerField(verbose_name="Harga Ecer",default=0,null=False,blank=False)	
	jumlah_barang = models.PositiveIntegerField(default=0)
	discount = models.IntegerField(default=0)
	rupiah_discount = models.PositiveIntegerField(default=0)
	sub_total = models.PositiveBigIntegerField(default=0)
	total = models.PositiveBigIntegerField(default=0)
	status_bayar = models.BooleanField(default=False)
	tanggal_trx = models.DateField(auto_now=True)

class Pembayaran(models.Model):
	pilihan_bayar = [
		('T','Tunai'),
		('C','Card (Credit/Debit)')
	]
	nomor_nota = models.CharField(max_length=12,default="0")
	metode_bayar = models.CharField(max_length=1,choices=pilihan_bayar,default="T")
	nomor_kartu = models.CharField(max_length=20,default="-")
	total_belanja = models.PositiveBigIntegerField(default=0)
	jumlah_dibayarkan = models.PositiveSmallIntegerField(default=0)
	kembalian_pembayaran = models.IntegerField(default=0)

class Penjualan_Stok_Keluar(models.Model):
	nomor_nota = models.CharField(max_length=12,default="0")
	id_barang = models.ForeignKey(MasterBarang,on_delete=models.RESTRICT)
	stok_jual = models.IntegerField(default=0)

class Pembelian_NomorNota(models.Model):
	nomor_nota = models.CharField(max_length=50,default="0")
	tanggal_nota = models.DateField(blank=False,null=False,default="2022-01-01")
	tanggal_jtempo = models.DateField(blank=False,null=False,default="2022-01-01")
	kode_supplier = models.ForeignKey(MasterSupplier,blank=False,null=False,on_delete=models.RESTRICT)
	proses = models.BooleanField(default=False)
	
	def __str__(self):
		return "[%s] [%s] [%s]"%(self.nomor_nota,self.tanggal_nota,self.kode_supplier)

	class Meta:
		unique_together = ['nomor_nota','kode_supplier','tanggal_nota']
		ordering = ['tanggal_nota','nomor_nota']

class Pembelian_Detail(models.Model):
	nomor_nota = models.ForeignKey(Pembelian_NomorNota,null=False,blank=False,on_delete=models.RESTRICT)
	kode_barang = models.ForeignKey(MasterBarang,blank=False,null=False,on_delete=models.RESTRICT)
	jumlah_barang = models.PositiveIntegerField(blank=False,null=False,default=0)
	harga_barang = models.PositiveBigIntegerField(blank=False,null=False,default=0)
	sub_total_harga = models.PositiveBigIntegerField(default=0)
	disc_persen = models.PositiveIntegerField(blank=False,null=False,default=0)
	disc_rupiah = models.PositiveIntegerField(default=0)
	pajak_persen = models.PositiveIntegerField(blank=False,null=False,default=0)
	pajak_rupiah = models.PositiveBigIntegerField(default=0)
	total_harga = models.PositiveBigIntegerField(default=0)
	proses = models.BooleanField(null=False,blank=False,default=False)

	def __str__(self):
		return "[%s] - %s - %i"%(self.nomor_nota,self.kode_barang,self.jumlah_barang)
