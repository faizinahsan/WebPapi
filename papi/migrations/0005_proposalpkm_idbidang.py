# Generated by Django 2.1.7 on 2019-04-08 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0004_bidangpkm'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalpkm',
            name='idBidang',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='papi.BidangPKM'),
        ),
    ]