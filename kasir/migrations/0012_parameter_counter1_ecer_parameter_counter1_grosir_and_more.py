# Generated by Django 4.1.3 on 2022-12-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0011_alter_parameter_id_sistem'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='counter1_ecer',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter1_grosir',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter2_ecer',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter2_grosir',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter3_ecer',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter3_grosir',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parameter',
            name='counter_nota',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
