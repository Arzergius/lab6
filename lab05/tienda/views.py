from django.shortcuts import render

from .models import Producto
# Create your views here.
def index(request):
    lista_productos = Producto.objects.all()
    context = {
        'productos':lista_productos
    }
    return render(request,'index.html')