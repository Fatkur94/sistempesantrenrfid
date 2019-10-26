from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from .santri import Santri

class Keluar(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    no_invoice = models.CharField(max_length=30, null=True, blank=True)
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE, null=True, blank=True)
    pilihan_keluar = (
        ('Periksa di Rumah Sakit', 'Periksa di Rumah Sakit'),
        ('Periksa di Puskesmas', 'Periksa di Puskesmas'),
        ('Belanja di Pasar', 'Belanja di Pasar'),
        ('Lain-Lain', 'Lain-Lain')
    )
    keperluan = models.CharField(max_length=30, choices=pilihan_keluar)
    keterangan = models.TextField(max_length=999, null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    pilihan_status = (
        ('Started', 'Masih keluar'),
        ('Ended', 'Selesai')
    )
    status = models.CharField(max_length=20, choices=pilihan_status)
    pilihan_durasi = (
        (timedelta(minutes=15), '15 menit'),
        (timedelta(minutes=30), '30 menit'),
        (timedelta(hours=1), '1 jam'),
        (timedelta(hours=2), '2 jam'),
        (timedelta(hours=3), '3 jam'),
        (timedelta(hours=5), '5 jam'),
        (timedelta(hours=10), '10 jam'),
    )
    masa_durasi = models.DurationField(null=True, blank=True, choices=pilihan_durasi)
    durasi_habis = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    sisa_waktu = models.DurationField(null=True, blank=True)

    def __str__(self):
        return self.keperluan