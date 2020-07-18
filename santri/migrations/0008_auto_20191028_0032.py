# Generated by Django 2.2.6 on 2019-10-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0007_auto_20191026_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='santri',
            name='dibuat_tanggal',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='anggotakeluarga',
            name='status',
            field=models.CharField(choices=[('Ayah', 'Ayah'), ('Ibu', 'Ibu'), ('Kakak', 'Kakak'), ('Adik', 'Adik'), ('Ayah Tiri', 'Ayah Tiri'), ('Ibu Tiri', 'Ibu Tiri'), ('Kakak Tiri', 'Kakak Tiri'), ('Adik Tiri', 'Adik Tiri')], max_length=10),
        ),
        migrations.AlterField(
            model_name='keluar',
            name='no_invoice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='pulang',
            name='no_invoice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sambang',
            name='no_invoice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='santri',
            name='pendidikan_terakhir',
            field=models.CharField(choices=[('TK', 'Taman Kanak-kanak'), ('SD', 'Sekolah Dasar'), ('SMP/MTs', 'Sekolah Menengah Pertama'), ('SMA/MA', 'Sekolah Menengah Atas'), ('D1/D2/D3', 'Diploma'), ('S1', 'SARJANA'), ('S2', 'MAGISTER'), ('S3', 'DOKTOR')], max_length=10),
        ),
        migrations.AlterField(
            model_name='santri',
            name='tanggal_masuk',
            field=models.DateField(blank=True, null=True),
        ),
    ]