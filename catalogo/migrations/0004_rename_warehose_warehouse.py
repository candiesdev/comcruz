# Generated by Django 4.2.11 on 2024-05-07 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_product_reseller_warehose_product_brand_brand_state_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Warehose',
            new_name='Warehouse',
        ),
    ]