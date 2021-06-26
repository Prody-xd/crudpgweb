from django.http import request
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.


def home(request):
  #Vehiculos viene desde la BD
  #crear un obj que me trae todas las entradas de la BD
  Vehiculos = Vehiculo.objects.all()
  datos = { 'Vehiculos' : Vehiculos }   
  return render(request,'core/home.html', datos)

def add_vehiculo(request):
  #request normal
    datos={
        'form': VehiculoForm(),
        }

    if request.method == 'POST':
      formulario_add = VehiculoForm(request.POST)
      if formulario_add.is_valid:
        formulario_add.save()
        datos['mensaje'] = "Datos guardados correctamente"

    return render (request, 'core/add_vehiculo.html', datos )

def edit_vehiculo(request, pk):
  vehiculo = Vehiculo.objects.get(patente=pk)
  datos = {
      'form': VehiculoForm(instance=vehiculo)
      }
  if request.method == 'POST':
      formulario_edit = VehiculoForm(data=request.POST, instance=Vehiculo)
      if formulario_edit.is_valid:
        formulario_edit.save()
        datos['mensaje'] = "Vehiculo Editado Correctamente"
  return render(request, 'core/edit_vehiculo.html', datos)

def delete_vehiculo(request, pk):
  vehiculos = Vehiculo.objects.get(patente = pk)
  vehiculos.delete()
  return redirect(to="home")

def formulario(request):
  return render(request, 'core/formulario.html')