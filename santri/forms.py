from django import forms
from .models.santri import Santri
from .models.anggota_keluarga import AnggotaKeluarga
from .models.keluar import Keluar
from .models.pulang import Pulang


class SantriForm(forms.ModelForm):
    class Meta:
        model = Santri
        fields = [
            'image', 'nama', 'gender', 'id_tag', 'no_induk', 'no_nik', 'no_kk', 'tempat_lahir', 
            'tanggal_lahir', 'agama', 'anak_ke', 'dari', 'no_telp', 'pendidikan_terakhir', 
            'provinsi', 'kota', 'kecamatan', 'alamat', 
        ]

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