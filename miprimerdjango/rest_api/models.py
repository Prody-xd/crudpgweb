from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class mecanicos (models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    telefono = models.CharField(max_length=250, verbose_name='Telefono')
    email = models.EmailField(max_length=250, verbose_name='Email')
    especialidad = models.CharField(max_length=250, verbose_name='Especialidad')
    tiempo_exp = models.CharField(max_length=250, verbose_name='Tiempo de Experiencia')
    def __str__(self):
        return self.nombre