# Generated by Django 4.2.11 on 2024-05-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_alter_product_catalog_warranty_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_inventory',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]