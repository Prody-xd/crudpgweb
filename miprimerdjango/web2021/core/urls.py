from django.urls import path
#from .views import gome, detalle, contacto
from .views import ejApi

urlpatterns = [
    path('', ejApi, name='ej-apis')
]