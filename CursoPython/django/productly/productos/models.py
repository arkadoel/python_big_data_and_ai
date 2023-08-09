from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255) #cadena de texto limitada
    
    def __str__(self):
        """devuelve la clase como string"""
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: eliminar el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina la categoria si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna el valor por defecto 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """devuelve la clase como string"""
        return str(self.nombre)
