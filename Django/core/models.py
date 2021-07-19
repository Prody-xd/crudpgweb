from django.db import models

# Create your models here.

#Modelo para login
class Login(models.Model):
    idLogin = models.IntegerField(primary_key=True, verbose_name='Id del Login')
    nombreLogin = models.CharField(max_length=50, verbose_name="Nombre del Login")

    def __str__(self):
        return self.nombreLogin

#Modelo para registro del vehiculo

class Registro(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo del Automovil')
    Categoria = models.ForeignKey(Login, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

class Categorias(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de la categoria')
    nombreCategoria = models.CharField(max_length=20, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria
    
#clase mecanico para api

class mecanico (models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, primary_key=True)
    email = models.CharField(max_length=80)
    website = models.CharField(max_length=100)