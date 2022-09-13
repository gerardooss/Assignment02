from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_catalog(request):
    katalogTerdaftar = CatalogItem.objects.all()
    context = {
    'list_barang': katalogTerdaftar,
    'nama': 'Marcelinus Gerardo',
    'npm' : '2106708324'
    }
    return render(request, "katalog.html", context)