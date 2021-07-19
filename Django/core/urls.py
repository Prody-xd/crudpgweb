from django.urls import path 
from .views import home
from .views import login
from .views import vehiculos
from .views import acuerdos



urlpatterns = [
    path('Home', home, name='home'),
    path('Iniciar-Sesion', login, name='Inicio-sesion'),
    path('Formulario', vehiculos, name='Registro vehiculos'),
    path('Terminos',acuerdos, name='Terminos y Condiciones' ),
   
]