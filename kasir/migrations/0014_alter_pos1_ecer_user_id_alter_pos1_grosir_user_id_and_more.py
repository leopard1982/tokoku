# Generated by Django 4.1.3 on 2022-12-01 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0013_pos1_ecer_total_pos1_grosir_total_pos2_ecer_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos1_ecer',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='pos1_grosir',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='pos2_ecer',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='pos2_grosir',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='pos3_ecer',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='pos3_grosir',
            name='user_id',
            field=models.CharField(default='-', max_length=100),
        ),
    ]