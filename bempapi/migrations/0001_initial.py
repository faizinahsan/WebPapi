# Generated by Django 2.2.1 on 2019-06-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormatProposalPKM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaBidang', models.CharField(max_length=50)),
                ('documentFormat', models.FileField(default='ProposalDefault.txt', upload_to='format')),
            ],
        ),
    ]
