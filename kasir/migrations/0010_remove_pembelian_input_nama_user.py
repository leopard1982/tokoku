# Generated by Django 4.1.3 on 2022-12-17 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0009_pembelian_posting_pembelian_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pembelian_input',
            name='nama_user',
        ),
    ]
