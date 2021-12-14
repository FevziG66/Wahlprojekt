# Generated by Django 3.2.9 on 2021-12-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belegdatum', models.DateField()),
                ('faelligkeit', models.DateField()),
                ('betrag', models.DecimalField(decimal_places=2, max_digits=10)),
                ('beschreibung', models.CharField(max_length=150)),
            ],
        ),
    ]
