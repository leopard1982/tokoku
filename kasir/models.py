from django.db import models

from django.urls import reverse

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

	def __str__(self):
		return "%s - %s"%(self.kode_supplier,self.nama_supplier)

	def delete_master(self):
		return reverse('Delete_Master_Supplier',args=[str(self.kode_supplier)])

	class Meta:
		unique_together=["kode_supplier","nama_supplier"]
		ordering = ["kode_supplier","nama_supplier"]

class MasterPelanggan(models.Model):
	pilihan = [('A','Pelanggan Harga#1'),('B','Pelanggan Harga#2'),('C','Pelanggan Harga#3')
	]
	kode_pelanggan = models.CharField(max_length=100,verbose_name="Kode Pelanggan",null=False,blank=False,primary_key=True)
	nama_pelanggan = models.CharField(max_length=100,verbose_name="Nama Pelanggan",null=False,blank=False)
	nomor_tlp = models.CharField(max_length=15,verbose_name="Nomor Telepon",null=False,blank=False)
	alamat_pelanggan = models.CharField(max_length=100,verbose_name="Alamat KTP",null=False,blank=False)
	foto_ktp = models.ImageField(verbose_name="Foto KTP",upload_to="ktp",null=False,blank=False)
	tipe = models.CharField(max_length=1,choices=pilihan,verbose_name="Tipe Pelanggan",null=False,blank=False)

	def __str_(self):
		return "%s - %s"%(self.kode_pelanggan,self.nama_pelanggan)

	class Meta:
		ordering = ['kode_pelanggan','nama_pelanggan']