# Generated by Django 2.1.7 on 2019-04-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0003_proposalpkm_idkategori'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidangPKM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaBidang', models.CharField(max_length=50)),
            ],
        ),
    ]
