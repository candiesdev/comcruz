# Generated by Django 4.2.11 on 2024-04-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_catalog',
            name='information',
            field=models.TextField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_catalog',
            name='product_state',
            field=models.CharField(choices=[('active', 'Activo'), ('inactive', 'Inactivo'), ('canceled', 'Cancelado')], default='active', max_length=50),
        ),
        migrations.AddField(
            model_name='product_inventory',
            name='inventory_state',
            field=models.CharField(choices=[('available', 'Disponible'), ('reserved', 'Reservado'), ('inactive', 'Inactivo'), ('canceled', 'Cancelado')], default='available', max_length=50),
        ),
        migrations.AddField(
            model_name='product_inventory',
            name='store',
            field=models.CharField(choices=[('locala', 'Local A'), ('digicorp', 'Digicorp')], default='locala', max_length=50),
        ),
        migrations.AlterField(
            model_name='product_catalog',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
