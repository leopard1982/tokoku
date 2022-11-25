# Generated by Django 4.1.3 on 2022-11-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0004_masterbarang_hapus_masterpelanggan_hapus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterParameter',
            fields=[
                ('kode_sistem', models.CharField(default='LT001', max_length=5, primary_key=True, serialize=False)),
                ('nomor_nota', models.PositiveBigIntegerField(default=1)),
                ('nota_POS1', models.PositiveBigIntegerField(default=1)),
                ('nota_POS2', models.PositiveBigIntegerField(default=1)),
                ('nota_POS3', models.PositiveBigIntegerField(default=1)),
            ],
        ),
    ]
