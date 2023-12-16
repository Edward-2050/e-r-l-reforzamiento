from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=25)
    numero = models.IntegerField()
    generacion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)