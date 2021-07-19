from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')
@login_required
def login(request):
    return render(request, '/registration/login.html') 
@login_required
def vehiculos(request):
    return render(request, 'core/vehiculos.html')
@login_required
def acuerdos(request):
    return render(request, 'core/acuerdos.html')
@login_required
def inicio(Request):
    return HttpResponse('Hola a todos')


