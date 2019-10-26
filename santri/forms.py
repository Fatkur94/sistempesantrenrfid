from django import forms
from .models.anggota_keluarga import AnggotaKeluarga
from .models.keluar import Keluar
from .models.pulang import Pulang

class AnggotaKeluargaForm(forms.ModelForm):
    
    class Meta:
        model = AnggotaKeluarga
        fields = ['nama', 'gender', 'id_tag', 'status', 'no_nik', 'no_kk', 'agama', 'no_telp', 'alamat', 'provinsi', 'kota', 'kecamatan', 'image']
        labels = {
            'no_telp': 'No Telepon',
        }

class KeluarForm(forms.ModelForm):
    class Meta:
        model = Keluar
        fields = ['keperluan', 'keterangan', 'masa_durasi', 'status']

class PulangForm(forms.ModelForm):
    class Meta:
        model = Pulang
        fields = ['keperluan', 'keterangan', 'masa_durasi', 'anggotakeluarga']

    def __init__(self, *args, **kwargs):
        santri = kwargs.pop('user') 
        super(PulangForm, self).__init__(*args, **kwargs)
        self.fields['anggotakeluarga'].queryset = AnggotaKeluarga.objects.filter(santri_id=5)