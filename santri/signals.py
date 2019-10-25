from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models.keluar import Keluar
from .models.pulang import Pulang
from .models.sambang import Sambang

@receiver(post_save, sender=Keluar)
def save_keluar(sender, instance, **kwargs):
    keluar = Keluar.objects.filter(id=instance.id)
    keluar.update(status='Started', durasi_habis=keluar[0].start_time + keluar[0].masa_durasi)

@receiver(post_save, sender=Pulang)
def save_pulang(sender, instance, **kwargs):
    pulang = Pulang.objects.filter(id=instance.id)
    pulang.update(status='Started', durasi_habis=pulang[0].start_time + pulang[0].masa_durasi)

@receiver(post_save, sender=Sambang)
def save_sambang(sender, instance, **kwargs):
    sambang = Sambang.objects.filter(id=instance.id)
    sambang.update(status='Started', status_penjenguk = sambang[0].penjenguk.status ,durasi_habis=sambang[0].start_time + sambang[0].masa_durasi)
    