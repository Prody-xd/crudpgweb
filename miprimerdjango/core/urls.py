from django.urls import path
from .views import form_vehiculo, home

urlpatterns=[ 
    path('',home, name="home"),
    path('form-vehiculo/',form_vehiculo, name= 'form_vehiculo'),
]