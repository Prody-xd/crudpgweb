from django.contrib import admin
from .models import Login, Registro
from .models import Categorias
from .models import mecanico

# Register your models here.

admin.site.register(Login)
admin.site.register(Registro)
admin.site.register(Categorias)
admin.site.register(mecanico)
