# Generated by Django 2.2.6 on 2019-10-26 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('santri', '0003_sambang'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggotakeluarga',
            name='id_tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='keluar',
            name='sisa_waktu',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='keluar',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pulang',
            name='sisa_waktu',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pulang',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sambang',
            name='sisa_waktu',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sambang',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='santri',
            name='id_tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sambang',
            name='status',
            field=models.CharField(choices=[('Started', 'Masih sambang'), ('Ended', 'Selesai')], max_length=20),
        ),
    ]
