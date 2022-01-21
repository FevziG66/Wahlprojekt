# Generated by Django 3.2.8 on 2022-01-21 15:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='art',
            field=models.CharField(choices=[('Einnahme', 'Einnahme'), ('Ausgabe', 'Ausgabe')], default='Einnahme', max_length=20),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='belegdatum',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='faelligkeit',
            field=models.DateField(default=datetime.date.today),
        ),
    ]