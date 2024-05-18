from django.db import models

# Create your models here.

# Modelo para registrar las marcas del catálogo
class Product_brand(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_states = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("canceled", "Cancelado"),
    ]
    brand_state = models.CharField(max_length=50, choices=brand_states, default='active')

    def __str__(self):
        return self.brand_name

# Modelo para registrar los revendedores de las marcas
class Product_reseller(models.Model):
    reseller_name = models.CharField(max_length=100)
    reseller_states = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("canceled", "Cancelado"),
    ]
    reseller_state = models.CharField(max_length=50, choices=reseller_states, default='active')

    def __str__(self):
        return self.reseller_name

# Modelo para registrar el catálogo de productos que se ofrecerán al mercado
class Product_catalog(models.Model):
    brand = models.ForeignKey(Product_brand, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100)
    information = models.TextField(max_length=500)
    warranty_days = models.IntegerField(default=0)
    product_states = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("canceled", "Cancelado"),
    ]
    product_state = models.CharField(max_length=50, choices=product_states, default='active')

    def __str__(self):
        return f"{self.brand} - {self.part_number} - {self.sku} - {self.description} - {self.product_state}"

# Modelo para registrar las bodegas adonde se almacenarán los productos
class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=100, unique=True)
    warehouse_classes = [
        ("own", "Propio"),
        ("external", "Externo"),
    ]
    warehouse_class = models.CharField(max_length=50, choices=warehouse_classes, default='external')
    warehouse_location = models.CharField(max_length=200)
    warehouse_states = [
        ("active", "Activo"),
        ("inactive", "Inactivo"),
        ("canceled", "Cancelado"),
    ]
    warehouse_state = models.CharField(max_length=50, choices=warehouse_states, default='active')

    def __str__(self):
        return self.warehouse_name

# Modelo para registrar el inventario disponible para la venta
class Product_inventory(models.Model):
    sku = models.ForeignKey(Product_catalog, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    available = models.IntegerField()
    reserved = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str_(self):
        return f"{self.sku} - {self.warehouse} - {self.available} - {self.reserved}"

# Modelo con las imágenes relacionadas a cada producto
class Product_img(models.Model):
    sku = models.ForeignKey(Product_catalog, on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='catalog_img/')
    main_img = models.BooleanField(default=False)

# Modelo que registrará transacciones y movimientos de productos
class Transactions(models.Model):
    transaction_logs = models.TextField(max_length=500)

    def __str__(self):
        return self.transaction_logs