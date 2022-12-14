# Generated by Django 4.1.3 on 2022-12-14 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kasir', '0002_rename_user_id_pos1_ecer_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pos1_ecer',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos1_ecer',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos1_ecer',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='pos1_grosir',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos1_grosir',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos1_grosir',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='pos2_ecer',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos2_ecer',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos2_ecer',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='pos2_grosir',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos2_grosir',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos2_grosir',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='pos3_ecer',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos3_ecer',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos3_ecer',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='pos3_grosir',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='pos3_grosir',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='pos3_grosir',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='harga_barang',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='nama_barang',
        ),
        migrations.RemoveField(
            model_name='posting',
            name='tanggal_nota',
        ),
        migrations.AddField(
            model_name='posting',
            name='total',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pos1_ecer',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='pos1_grosir',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='pos2_ecer',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='pos2_grosir',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='pos3_ecer',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='pos3_grosir',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='id_barang',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to='kasir.masterbarang'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='kode_sistem',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='posting',
            name='userid',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
