# Generated by Django 2.2 on 2019-05-20 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0025_auto_20190509_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anggota',
            name='idPkm',
        ),
    ]
