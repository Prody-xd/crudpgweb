from django.contrib import admin
from .models import categoria, Vehiculo, mecanicos

# Register your models here.
admin.site.register(categoria)
admin.site.register(Vehiculo)
admin.site.register(mecanicos)
