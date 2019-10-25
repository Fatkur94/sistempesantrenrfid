from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from .santri import Santri
from .anggota_keluarga import AnggotaKeluarga

class Pulang(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE, null=True, blank=True)
    anggotakeluarga = models.ForeignKey(AnggotaKeluarga, on_delete=models.CASCADE, null=True, blank=True)
    pilihan_pulang = (
        ('Periksa di Rumah Sakit', 'Periksa di Rumah Sakit'),
        ('Periksa di Puskesmas', 'Periksa di Puskesmas'),
        ('Hajatan - Nikah', 'Hajatan - Nikah'),
        ('Hajatan - Meninggal', 'Hajatan - Meninggal'),
        ('Lain-Lain', 'Lain-Lain')
    )
    keperluan = models.CharField(max_length=30, choices=pilihan_pulang)
    keterangan = models.TextField(max_length=999, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    pilihan_status = (
        ('Started', 'Masih berjalan'),
        ('Ended', 'Selesai')
    )
    status = models.CharField(max_length=20, choices=pilihan_status)
    pilihan_durasi = (
        (timedelta(days=1), '1 hari'),
        (timedelta(days=2), '2 hari'),
        (timedelta(days=3), '3 hari'),
        (timedelta(days=5), '5 hari'),
        (timedelta(days=7), '7 hari(1 minggu)'),
        (timedelta(days=14), '14 hari(2 minggu)'),
        (timedelta(days=30), '30 hari(1 bulan)'),
    )
    masa_durasi = models.DurationField(null=True, blank=True, choices=pilihan_durasi)
    durasi_habis = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)