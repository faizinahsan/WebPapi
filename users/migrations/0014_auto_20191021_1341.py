# Generated by Django 2.2.4 on 2019-10-21 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191021_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                       primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
