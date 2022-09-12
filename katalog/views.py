from django.shortcuts import render
from katalog.models import CatalogItem

data_catalog_item = CatalogItem.objects.all()
context = {
    'list_barang': data_catalog_item,
    'nama': 'Rahma Adinda',
    'ID': '2106750774'
}

def show_katalog(request):
    return render(request, "katalog.html", context)