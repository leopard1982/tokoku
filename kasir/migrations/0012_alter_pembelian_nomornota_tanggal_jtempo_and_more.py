# Generated by Django 4.1.3 on 2022-12-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0011_pembelian_detail_pembelian_nomornota_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembelian_nomornota',
            name='tanggal_jtempo',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='pembelian_nomornota',
            name='tanggal_nota',
            field=models.DateField(default='2022-01-01'),
        ),
    ]