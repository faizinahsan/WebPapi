# Generated by Django 2.1.7 on 2019-04-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0018_auto_20190424_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalpkm',
            name='deskripsi',
            field=models.TextField(default=''),
        ),
    ]
