from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .santri import Santri
from .anggota_keluarga import AnggotaKeluarga
from datetime import timedelta


class Sambang(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE, null=True, blank=True)
    penjenguk = models.ForeignKey(AnggotaKeluarga, on_delete=models.CASCADE, null=True, blank=True)
    status_penjenguk = models.CharField(max_length=15, null=True, blank=True)
    menginap = models.BooleanField(default=False)
    keterangan = models.TextField(max_length=999, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    pilihan_status = (
        ('Started', 'Masih berjalan'),
        ('Ended', 'Selesai')
    )
    status = models.CharField(max_length=20, choices=pilihan_status)
    pilihan_durasi = (
        (timedelta(hours=1), '1 jam'),
        (timedelta(hours=2), '2 jam'),
        (timedelta(hours=3), '3 jam'),
        (timedelta(hours=5), '5 jam'),
        (timedelta(hours=10), '10 jam'),
        (timedelta(days=1), '1 hari'),
        (timedelta(days=2), '2 hari'),
        (timedelta(days=3), '3 hari'),
        (timedelta(days=5), '5 hari'),
        (timedelta(days=7), '7 hari(1 minggu)'),
    )
    masa_durasi = models.DurationField(null=True, blank=True, choices=pilihan_durasi)
    durasi_habis = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    sisa_waktu = models.DateTimeField(null=True, blank=True)

