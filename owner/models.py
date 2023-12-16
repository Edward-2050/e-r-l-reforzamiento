from django.db import models


# Create your models here.
class Owner(models.Model):
	nombre = models.CharField(max_length=25)
	edad = models.IntegerField(default=0)
	pais = models.CharField(max_length=27, default='')
	descripcion = models.TextField()