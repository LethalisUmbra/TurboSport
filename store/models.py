from django.db import models
from django.core.validators import *

# Create your models here.

class Producto(models.Model):
	id_producto = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100, validators=[MaxLengthValidator(100), MinLengthValidator(3)])
	categoria = models.CharField(max_length=50, validators=[MaxLengthValidator(50), MinLengthValidator(3)])
	tipo_producto = models.CharField(max_length=50, validators=[MaxLengthValidator(50), MinLengthValidator(3)])
	marca = models.CharField(max_length=50, null=True)
	precio = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
	talla = models.CharField(max_length=15, null=True)
	color = models.CharField(max_length=25, validators=[MaxLengthValidator(25), MinLengthValidator(3)])
	descripcion = models.TextField(null=True)
	imagen = models.ImageField(upload_to='uploads/', null=True)

	def __str__(self):
		return self.nombre