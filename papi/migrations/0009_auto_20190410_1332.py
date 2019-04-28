# Generated by Django 2.1.7 on 2019-04-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0008_auto_20190408_1437'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaAnggota', models.CharField(max_length=20)),
                ('emailAnggota', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bidangpkm',
            name='jumlahAnggota',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]