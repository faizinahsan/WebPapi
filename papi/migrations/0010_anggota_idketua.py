# Generated by Django 2.1.7 on 2019-04-10 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('papi', '0009_auto_20190410_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota',
            name='idKetua',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
