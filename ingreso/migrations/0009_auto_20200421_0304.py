# Generated by Django 3.0.4 on 2020-04-21 03:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0008_auto_20200420_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingreso',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de creación'),
        ),
    ]
