from django.db import models

# Create your models here.
class Catalog(models.Model):
    nombre = models.CharField(max_length=30, default='')
    tipo = models.CharField(max_length=25)
    habilidad = models.CharField(max_length=30)
    debilidad = models.CharField(max_length=30)

