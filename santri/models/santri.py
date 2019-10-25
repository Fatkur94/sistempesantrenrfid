from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from PIL import Image

class Santri(models.Model):
    nama = models.CharField(max_length=300)
    pilihan_gender = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    gender = models.CharField(max_length=20, choices=pilihan_gender)
    tanggal_lahir = models.DateField()
    tempat_lahir = models.CharField(max_length=50)
    anak_ke = models.IntegerField()
    dari = models.IntegerField(null=True, blank=True)
    pilihan_agama = (
        ('Islam', 'Islam'), 
        ('Kristen', 'Kristen'), 
        ('Katholik', 'Katholik'), 
        ('Hindu', 'Hindu'), 
        ('Budha', 'Budha'), 
        ('Konghucu', 'Konghucu')
    )
    agama = models.CharField(max_length=10, choices=pilihan_agama)
    regex = RegexValidator(regex=r'^\d[0-9 -]{4,50}$', message="format berupa: '999999/ 999 999 / 999-999', min:5 digit, maks: 50 digit" )
    no_induk = models.CharField(validators=[regex], max_length=55)
    no_nik = models.CharField(validators=[regex], max_length=55)
    no_kk = models.CharField(validators=[regex], max_length=55)
    phone = RegexValidator(regex=r'^\+?\d[0-9 -]{4,20}$', message="format berupa: '+999999 / +999 999 / +999-999, min:5 digit, maksimal 20 digit" )
    no_telp = models.CharField(validators=[phone], max_length=23 , null=True, blank=True)
    pilihan_pendidikan = (
        ('TK', 'Taman Kanak-kanak'),
        ('SD', 'Sekolah Dasar'),
        ('SMP/MTs', 'Sekolah Menengah Pertama'),
        ('SMA/MA', 'Sekolah Menengah Atas')
    )
    pendidikan_terakhir = models.CharField(max_length=10, choices=pilihan_pendidikan)
    alamat = models.TextField(max_length=300)
    provinsi = models.CharField(max_length=50)
    kota = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='santri_pics')
    tanggal_masuk = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama
        
    def get_absolute_url(self):
        return reverse('santri-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)