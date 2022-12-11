from django import forms

from .models import MasterSupplier, MasterPelanggan, MasterBarang

class InputMasterSupplier(forms.ModelForm):
	class Meta:
		model=MasterSupplier
		fields = "__all__"
		exclude= ['hutang_tambahan','hutang_akhir','hapus']

		widgets= {
			'kode_supplier':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nama_supplier':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'tlp1':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'tlp2':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'alamat':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'hutang_awal':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'catatan':forms.TextInput(attrs={'class':'form-control input-lg'})
		}

class InputMasterPelanggan(forms.ModelForm):
	class Meta:
		model=MasterPelanggan
		fields = "__all__"
		exclude = ['hapus']

		widgets= {
			'kode_pelanggan': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nama_pelanggan': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nomor_tlp' : forms.TextInput(attrs={'class':'form-control input-lg'}),
			'alamat_pelanggan' : forms.TextInput(attrs={'class':'form-control input-lg'})
		}

class InputMasterBarang(forms.ModelForm):
	class Meta:
		model=MasterBarang
		fields = "__all__"
		exclude = ['stok_beli','stok_rusak','stok_akhir','hapus']

		widgets = {
			'id_barang': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nama_barang' :forms.TextInput(attrs={'class':'form-control input-lg'}),
			'stok_awal': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'harga_modal':forms.TextInput(attrs={'class':'form-control input-lg'}),
			'harga_ecer': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'harga_grosir1': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'harga_grosir2': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'harga_grosir3': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'keterangan_isi' : forms.TextInput(attrs={'class':'form-control input-lg'}),
		}

class InputPOS_ecer1(forms.ModelForm):
	pass 
		