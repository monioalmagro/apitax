# Generated by Django 3.0.4 on 2020-04-20 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingreso', '0002_auto_20200419_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=50, verbose_name='cuenta')),
                ('categoria', models.CharField(max_length=50, verbose_name='categoria')),
                ('signo', models.CharField(max_length=3, verbose_name='signo')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=50, verbose_name='cuenta')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('signo', models.CharField(max_length=50, verbose_name='signo')),
                ('detalle', models.CharField(max_length=50, verbose_name='detalle')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='fecha',
            field=models.DateTimeField(verbose_name='Fecha de creación'),
        ),
    ]
