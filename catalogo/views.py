from django.shortcuts import render, get_object_or_404
from .models import Product_catalog, Product_inventory, Product_img

# Create your views here.

# Retorna el inventario solicitado
def inventory_data(type):
    if type == "tools_full": # Retorna el inventario total disponible para la categoría herramientas (tools_full)
        inventory_list = {}
        inventory_list_updated = {}
        inventory_full = Product_inventory.objects.filter(available__gt=0) # Crea el objeto con el listado total de productos que tengan mas de una unidad disponible
        for inventory in inventory_full: # Itera el objeto para conseguir el precio y URL de las imágenes por sku y crear el diccionario product_details para cada producto
            product_sku=inventory.sku.sku
            product_details = {}
            product_details["price"] = inventory.price
            objeto = get_object_or_404(Product_img, sku=inventory.sku.id, main_img=True) # Crea un nuevo objeto para extraer el URL de la imagen principal, en mejoras posteriores se podrán utilizar múltiples imágenes
            img_url = objeto.product_img.url
            product_details["img_url"] = img_url
            inventory_list[product_sku] = product_details # Se agrega a la lista de inventario el diccionario con precio y URL del producto
        for productsku, productdetails in inventory_list.items(): # Se crea un nuevo objeto con detalles del producto disponibles en el catálogo
            product_detail = Product_catalog.objects.get(sku=productsku)
            productdetails["brand"] = product_detail.brand.brand_name
            productdetails["part_number"] = product_detail.part_number
            productdetails["description"] = product_detail.description
            productdetails["information"] = product_detail.information
            inventory_list_updated[productsku] = productdetails # Se agregan al diccionario de productos la marca, número de parte, descripcion e información ampliada
        inventory_list = inventory_list_updated # Se actualiza la lista de inventario con la información de productos agregada
    return(inventory_list)

# Función principal de la vista del catálogo
def index(request):
    inventory_list = inventory_data("tools_full")
    head_addon = """
    <link rel='stylesheet' href='/static/catalogo/css/catalogo_styles.css'>
    """
    return render(request, "catalogo/index.html", {"inventory": inventory_list, "head_addons": head_addon})