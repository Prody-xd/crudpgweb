from django.db import models

# Create your models here.

#modelo para categoria
class categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

#modelo para vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca del vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='modelo del auto')
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

class mecanicos (models.Model):
    nombre = models.CharField(max_length=250, verbose_name='Nombre')
    telefono = models.CharField(max_length=250, verbose_name='Telefono')
    email = models.CharField(max_length=250, verbose_name='Email')
    especialidad = models.CharField(max_length=250, verbose_name='Especialidad')
    tiempo_exp = models.CharField(max_length=250, verbose_name='Tiempo de Experiencia')
    def __str__(self):
        return self.nombre