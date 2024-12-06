from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveIntegerField()
    correo=models.EmailField(max_length=100)

    def __str__(self):
        return self.nombre
