# Generated by Django 2.1.7 on 2019-04-25 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190425_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fakultas',
            name='idJurusan',
        ),
        migrations.AddField(
            model_name='jurusan',
            name='idFakultas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Jurusan'),
        ),
    ]
