# Generated by Django 2.1.7 on 2019-04-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalpkm',
            name='document',
            field=models.FileField(default='ProposalDefault.txt', upload_to='proposal'),
        ),
    ]