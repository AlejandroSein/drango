from django.db import models

# Create your models here.

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagenes', null=True)
    descripcion = models.TextField(max_length=500, verbose_name='Descripcion', null=True)