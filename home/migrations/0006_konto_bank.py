# Generated by Django 3.2.9 on 2022-01-04 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_konto_receipt_konto_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='konto',
            name='bank',
            field=models.CharField(default='SpardaBank', max_length=40),
            preserve_default=False,
        ),
    ]