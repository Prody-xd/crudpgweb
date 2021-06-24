from django.shortcuts import render
from .models import Vehiculo

# Create your views here.


def home(request):
  #Vehiculos viene desde la BD
  #crear un obj que me trae todas las entradas de la BD
  Vehiculos = Vehiculo.objects.all()
  datos = { 'vehiculos' : Vehiculos }   
  return render(request,'core/home.html', datos)

def form_vehiculo(request):
    return render (request, 'core/form_vehiculo.html' )