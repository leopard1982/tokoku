from django import forms

from .models import MasterSupplier, MasterPelanggan, MasterBarang, Pembelian_NomorNota, Pembelian_Detail

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

class InputPembelianNomorNota(forms.ModelForm):
	class Meta:
		model = Pembelian_NomorNota
		fields = ["nomor_nota","tanggal_nota","tanggal_jtempo","kode_supplier"]

		widgets = {
			'tanggal_nota':forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Tanggal Pembelian','type': 'date'}),
			'tanggal_jtempo':forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control', 'placeholder': 'Tanggal Jatuh Tempo','type': 'date'}),
			'nomor_nota':forms.TextInput(attrs={'class':'form-control'}),
			'kode_supplier':forms.Select(attrs={'class':'form-control'}),
		}
class InputPembelianDetail(forms.ModelForm):
	class Meta:
		model = Pembelian_Detail
		fields = "__all__"
		exclude=['sub_total_harga','disc_rupiah','pajak_rupiah','total_harga','posting']
		