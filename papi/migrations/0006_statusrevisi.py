# Generated by Django 2.1.7 on 2019-04-08 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0005_proposalpkm_idbidang'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusRevisi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaStatus', models.CharField(max_length=50)),
            ],
        ),
    ]