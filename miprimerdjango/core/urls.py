from django.urls import path
from .views import home, add_vehiculo, edit_vehiculo, delete_vehiculo, formulario 
from core import views


urlpatterns = [
    path('home/', home, name="home" ),
    path('agregar-vehiculo/', add_vehiculo, name='add-vehiculo'),
    path('editar-vehiculo/<pk>/', edit_vehiculo, name='edit-vehiculo'),
    path('delete-vehiculo/<pk>/', delete_vehiculo,name='delete-vehiculo'),
    path('formulario/', formulario, name='formulario'),
    path('inicio', views.inicio, name='inicio'),
    
]