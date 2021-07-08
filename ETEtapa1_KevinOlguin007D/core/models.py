from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Usuario(models.Model):

    rut = models.CharField(max_length=100, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    telefono = models.CharField(max_length=10, verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    email = models.CharField(max_length=30, verbose_name='Email')
    pais = models.CharField(max_length=10, verbose_name='Pais')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')
    image = models.ImageField(upload_to='images/', null=True)

    def str(self):

        return (self.rut)

