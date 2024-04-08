from django.db import models

# Create your models here.
class Producto (models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    categoria = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    precio = models.IntegerField(max_length = 7)
