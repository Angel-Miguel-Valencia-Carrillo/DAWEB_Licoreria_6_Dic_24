from django.shortcuts import render,redirect
from .models import Sucursal
# Create your views here.

def inicio_Sucursal(request):
    lassucursales=Sucursal.objects.all()
    return render(request,"gestionarSucursal.html",{"missucursales":lassucursales})

def registrarSucursal(request):
    id_sucursal=request.POST["txtid_sucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre=nombre,
        direccion=direccion,
        telefono=telefono,
        correo=correo,
    ) # GUARDA EL REGISTRO

    return redirect("inicio_Sucursal")

def seleccionarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request,"editarsucursal.html",{"missucursales":sucursal})

def editarSucursal(request):
    id_sucursal=request.POST["txtid_sucursal"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    correo=request.POST["txtcorreo"]
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre=nombre
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    sucursal.correo=correo
    sucursal.save() #guarda registro actualizado
    return redirect("inicio_Sucursal")

def borrarSucursal(request,id_sucursal):
    sucursal=Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete() #borrar el registro

    return redirect("inicio_Sucursal")

# Create your views here.
