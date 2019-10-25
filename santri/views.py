from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models.santri import Santri
from .models.anggota_keluarga import AnggotaKeluarga
from .models.keluar import Keluar
from .models.pulang import Pulang
from .models.sambang import Sambang
from .forms import AnggotaKeluargaForm, KeluarForm
from datetime import datetime
from django.urls import reverse_lazy

# Santri
class SantriListView(LoginRequiredMixin, ListView):
    model = Santri
    context_object_name = 'para_santri'
    ordering = '-tanggal_masuk'

class SantriDetailView(LoginRequiredMixin, DetailView):
    model = Santri 
    context_object_name = 'santri'

class SantriCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Santri
    fields = [
        'image', 'nama', 'gender', 'no_induk', 'no_nik', 'no_kk', 'tempat_lahir', 
        'tanggal_lahir', 'agama', 'anak_ke', 'dari', 'no_telp', 'pendidikan_terakhir', 
        'provinsi', 'kota', 'kecamatan', 'alamat', 
    ]
    success_message = 'Data santri berhasil dibuat'

class SantriUpdateView(LoginRequiredMixin ,UpdateView):
    model = Santri
    fields = [
        'image', 'nama', 'gender', 'no_induk', 'no_nik', 'no_kk', 'tempat_lahir', 
        'tanggal_lahir', 'agama', 'anak_ke', 'dari', 'no_telp', 'pendidikan_terakhir', 
        'provinsi', 'kota', 'kecamatan', 'alamat', 
    ]

class SantriDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Santri
    success_message = "Data Santri sudah dihapus"
    success_url = reverse_lazy('santri-list')


# Anggota Santri
class AnggotaKeluargaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AnggotaKeluarga
    fields = [
        'nama', 'gender', 'status', 'no_nik', 'no_kk', 'agama', 'no_telp', 'alamat',
        'provinsi', 'kota', 'kecamatan', 'image'
    ]
    success_message = "Data Anggota Keluarga telah dibuat"

    def form_valid(self, form):
        form.instance.santri = Santri.objects.get(id=self.kwargs['santri'])
        return super(AnggotaKeluargaCreateView, self).form_valid(form)

# update anggotakeluarga 
@login_required
def update_anggotakeluarga(request, santri, anggotakeluarga):
    anggotakeluarga = get_object_or_404(AnggotaKeluarga, id=anggotakeluarga)
    form = AnggotaKeluargaForm(instance=anggotakeluarga)
    if request.method == 'POST':
        form = AnggotaKeluargaForm(request.POST, instance=anggotakeluarga)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data anggota keluarga berhasil diperbarui')
            return redirect('santri-detail', pk=santri)
    return render(request, 'santri/anggotakeluarga_form.html', {'form':form})

# delete anggotakeluarga
@login_required
def delete_anggotakeluarga(request, santri, anggotakeluarga):
    if request.method == 'POST':
        get_object_or_404(AnggotaKeluarga, id=anggotakeluarga).delete()
        messages.success(request, 'Data anggota keluarga berhasil dihapus')
        return redirect('santri-detail', santri)

class KeluarCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Keluar
    fields = [
        'keperluan', 'keterangan', 'masa_durasi'
    ]
    success_message = "Data santri keluar telah dibuat"
    success_url = reverse_lazy('keluar-list')

    def get_context_data(self, *args, **kwargs):
        form = super(KeluarCreateView, self).get_context_data(*args, **kwargs)
        form['santri'] = Santri.objects.get(id=self.kwargs['pk'])
        return form
    
    def form_valid(self, form):
        form.instance.santri = Santri.objects.get(id=self.kwargs['pk'])
        return super(KeluarCreateView, self).form_valid(form)

class KeluarListView(LoginRequiredMixin, ListView):
    model = Keluar
    context_object_name = 'santri_keluar'
    ordering = '-start_time'

@login_required
def update_keluar(request, santri, keluar):
    keluar = Keluar.objects.filter(id=keluar).update(end_time=datetime.today(), status='Ended')
    messages.success(request, f'Santri {Santri.objects.get(id=santri)} telah kembali')
    return redirect('keluar-list')

class PulangCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Pulang
    fields = ['keperluan', 'keterangan', 'masa_durasi', 'anggotakeluarga']
    success_message = "Data santri Pulang telah dibuat"
    success_url = reverse_lazy('pulang-list')

    def get_context_data(self, *args, **kwargs):
        form = super(PulangCreateView, self).get_context_data(*args, **kwargs)
        form['santri'] = Santri.objects.get(id=self.kwargs['pk'])
        form['form'].fields['anggotakeluarga'].queryset = AnggotaKeluarga.objects.filter(santri=form['santri'])
        return form
    
    def form_valid(self, form):
        form.instance.santri = Santri.objects.get(id=self.kwargs['pk'])
        return super(PulangCreateView, self).form_valid(form)

class PulangListView(LoginRequiredMixin, ListView):
    model = Pulang
    context_object_name = 'santri_pulang'
    ordering = '-start_time'

@login_required
def update_pulang(request, santri, pulang):
    pulang = Pulang.objects.filter(id=pulang).update(end_time=datetime.today(), status='Ended')
    messages.success(request, f'Santri {Santri.objects.get(id=santri)} telah kembali')
    return redirect('pulang-list')

class SambangCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Sambang
    fields = ['penjenguk', 'menginap', 'keterangan', 'masa_durasi']
    success_message = "Data santri sambang telah dibuat"
    success_url = reverse_lazy('sambang-list')

    def get_context_data(self, *args, **kwargs):
        form = super(SambangCreateView, self).get_context_data(*args, **kwargs)
        form['santri'] = Santri.objects.get(id=self.kwargs['pk'])
        form['form'].fields['penjenguk'].queryset = AnggotaKeluarga.objects.filter(santri=form['santri'])
        return form
    
    def form_valid(self, form):
        form.instance.santri = Santri.objects.get(id=self.kwargs['pk'])
        return super(SambangCreateView, self).form_valid(form)

class SambangListView(LoginRequiredMixin, ListView):
    model = Sambang
    context_object_name = 'santri_sambang'
    ordering = '-start_time'

@login_required
def update_sambang(request, santri, sambang):
    sambang = Sambang.objects.filter(id=sambang).update(end_time=datetime.today(), status='Ended')
    messages.success(request, f'Santri {Santri.objects.get(id=santri)} sudah selesai disambang')
    return redirect('sambang-list')

def sambang_invoice(request, santri, sambang):
    obj = Sambang.objects.get(pk=sambang)
    return render(request, 'santri/sambang_invoice.html', {'obj':obj})

def invoice(request):
    return render(request, 'santri/invoice.html')