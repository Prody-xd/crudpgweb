from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.


def home(request):
  #Vehiculos viene desde la BD
  #crear un obj que me trae todas las entradas de la BD
  Vehiculos = Vehiculo.objects.all()
  datos = { 'Vehiculos' : Vehiculos }   
  return render(request,'core/home.html', datos)

def form_vehiculo(request):
  #request normal
    datos={
        'form': VehiculoForm(),
        }

    if request.method == 'POST':
      formulario = VehiculoForm(request.POST)
      if formulario.is_valid():
        formulario.save()
        datos['mensaje'] = "Datos guardados correctamente"

  
    return render (request, 'core/form_vehiculo.html', datos )

def form_mod_vehiculo(request, pk):
  vehiculo = get_object_or_404(Vehiculo, patente=pk)
  datos = {
      'form': VehiculoForm(instance=vehiculo)
  }
  return render(request, 'core/form_mod_vehiculo.html', datos)