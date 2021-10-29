
from django.shortcuts import render, redirect
from .models import Producto
from apps.tienda import Carrito


# Create your views here.


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/productos.html", {"productos": productos})

def agregar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=id_producto)
    carrito.agregar(producto)
    return redirect("tienda/productos.html")

def restar_producto(request, id_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto = id_producto)
    carrito.restar(producto)
    return redirect("tienda/productos.html")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda/productos.html")
