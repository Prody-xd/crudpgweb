from django.urls import path
from .views import form_vehiculo, home

urlpatterns=[ 
    path('',home, name="home"),
    path('add-vehiculo',form_vehiculo, name= 'add-vehiculo'),
]