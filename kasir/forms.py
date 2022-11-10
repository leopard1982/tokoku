from django import forms

from .models import MasterSupplier, MasterPelanggan

class InputMasterSupplier(forms.ModelForm):
	class Meta:
		model=MasterSupplier
		fields = "__all__"
		exclude= ['hutang_tambahan','hutang_akhir']

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

		widgets= {
			'kode_pelanggan': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nama_pelanggan': forms.TextInput(attrs={'class':'form-control input-lg'}),
			'nomor_tlp' : forms.TextInput(attrs={'class':'form-control input-lg'}),
			'alamat_pelanggan' : forms.TextInput(attrs={'class':'form-control input-lg'})
		}