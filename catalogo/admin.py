from django.contrib import admin

# Register your models here.

from .models import Product_brand, Product_reseller, Warehouse, Product_catalog, Product_inventory, Transactions, Product_img

admin.site.register(Product_brand)
admin.site.register(Product_reseller)
admin.site.register(Warehouse)
admin.site.register(Product_catalog)
admin.site.register(Product_inventory)
admin.site.register(Transactions)
admin.site.register(Product_img)