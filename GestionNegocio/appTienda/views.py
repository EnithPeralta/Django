from django.shortcuts import render,redirect
from appTienda.models import Categoria,Producto
from django.db import Error

# Create your views here.

def inicio(request):
    return render(request,"inicio.html")

def vistaCategorias(request):
    return render(request,"categorias.html")

def agregarCategoria(request):
    nombre = request.POST["nombre",""]
    try:
        categoria = Categoria(nombre=nombre)
        categoria.save()
        mensaje = "Categoria agregada correctamente"
    except:
        mensaje = "Problemas al agregar la categoria"
    retorno = {"mensaje":mensaje}
    return render(render,"agregar.html",retorno)

def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje = ""
        print(productos)
    except:
        mensaje = "Problemas al obtener los productos"
    retorno = {"mensaje":mensaje,"listarProductos":productos}
    return render(request,"listarProductos.html",retorno)

def vistarProducto(request):
    try:
        categorias = Categoria.objects.all()
        mensaje = ""
    except:
        mensaje = "Problemas al agregar la categoria"
    retorno ={"mensaje":mensaje,"listarCategoria":categorias, "producto":None}
    return render(request,"registarProducto.html",retorno)

def agregarProducto(request):
    nombre = request.POST["nombre"]
    codigo = int(request.POST["codigo"])
    precio = int(request.POST["precio"])
    idCategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES["fileFoto"]
    try:
        categoria = Categoria.objects.get(id=idCategoria)
        producto = Producto(
            nombre=nombre,
            codigo=codigo,
            precio=precio,
            categoria=categoria,
            foto = archivo
        )
        producto.save()
        mensaje = "Producto Agregado Correctamente"
        return redirect("/listarProductos/")
    except Error as error:
        mensaje = f"Problema al agregar el producto.{error}"

    categoria = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias":categoria,"producto":producto}
    return render(request,"registarProducto.html",retorno)