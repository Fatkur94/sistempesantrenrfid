# Generated by Django 2.2.6 on 2020-10-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('santri', '0008_auto_20191028_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='santri',
            name='id_tag',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]