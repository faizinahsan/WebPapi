# Generated by Django 2.1.7 on 2019-04-25 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190425_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahasiswa',
            name='fakultas',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Fakultas'),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='jurusan',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Jurusan'),
        ),
    ]
