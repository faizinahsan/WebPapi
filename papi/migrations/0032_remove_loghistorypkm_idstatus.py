# Generated by Django 2.2.1 on 2019-06-01 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0031_loghistorypkm_documentrevisi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loghistorypkm',
            name='idStatus',
        ),
    ]
