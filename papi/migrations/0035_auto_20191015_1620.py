# Generated by Django 2.2.6 on 2019-10-15 09:20

from django.db import migrations, models
import papi.validators


class Migration(migrations.Migration):

    dependencies = [
        ('papi', '0034_auto_20190601_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposalpkm',
            name='document',
            field=models.FileField(default='ProposalDefault.txt', upload_to='proposal', validators=[papi.validators.validate_file_extension]),
        ),
    ]
