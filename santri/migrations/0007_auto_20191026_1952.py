# Generated by Django 2.2.6 on 2019-10-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0006_auto_20191026_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='keluar',
            name='sisa_waktu',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pulang',
            name='sisa_waktu',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sambang',
            name='sisa_waktu',
            field=models.DurationField(blank=True, null=True),
        ),
    ]