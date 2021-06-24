from django.shortcuts import render
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.


def home(request):
  #Vehiculos viene desde la BD
  #crear un obj que me trae todas las entradas de la BD
  Vehiculos = Vehiculo.objects.all()
  datos = { 'vehiculos' : Vehiculos }   
  return render(request,'core/home.html', datos)

def form_vehiculo(request):
    formulario = VehiculoForm()
    datos={'formulario' : formulario}
    return render (request, 'core/form_vehiculo.html', datos )