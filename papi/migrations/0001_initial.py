# Generated by Django 2.1.7 on 2019-04-07 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoriPKM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaKategori', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalPKM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('namaKetua', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('bidang', models.CharField(max_length=20)),
                ('idUsers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
