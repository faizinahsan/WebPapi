# Generated by Django 2.2 on 2019-05-05 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190505_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='fakultas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Fakultas'),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='fakultas',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Fakultas'),
        ),
        migrations.AlterField(
            model_name='mahasiswa',
            name='jurusan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Jurusan'),
        ),
    ]
