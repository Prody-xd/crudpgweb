from core.models import mecanico
from django.urls import path
from .views import mecanicos, mecanic

urlpatterns = [
    path('mecanicos/', mecanicos, name="api_mecanicos"),
    path('mecanicos/<pk>', mecanic , name="mecanico")
]