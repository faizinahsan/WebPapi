# Generated by Django 2.1.7 on 2019-04-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190402_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaFakultas', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaJurusan', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='fakultas',
            name='idJurusan',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.Jurusan'),
        ),
    ]