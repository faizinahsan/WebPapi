# Generated by Django 2.2 on 2019-05-05 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20190505_2351'),
        ('papi', '0021_auto_20190505_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalpkm',
            name='idDosenReviewer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Dosen'),
        ),
    ]
