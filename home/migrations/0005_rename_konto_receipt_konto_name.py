# Generated by Django 3.2.9 on 2022-01-04 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_konto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='konto',
            new_name='konto_name',
        ),
    ]