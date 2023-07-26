from django.db import models

# Create your models here.

""" 
Aquí se almacenan los vehículos ingresados, son los campos requeridos del formulario y además 
la fecha de creación y modificación que se generan automáticamente al guardar.
"""

class Vehiculo(models.Model):
    marca = models.CharField(max_length=20, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, default='Particular')
    precio = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.marca} -> {self.modelo}'