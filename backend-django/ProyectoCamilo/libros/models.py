from django.db import models

# Create your models here.
class Libros(models.Model):
    nombre = models.CharField
    descripcion= models.CharField
    precio= models.FloatField
