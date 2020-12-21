from django.db import models
from django.core.validators import *

# Create your models here.

class Carrito(models.Model):
	id_carrito = models.AutoField(primary_key=True)
	producto = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])
	precio = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
	cliente = models.CharField(max_length=150, validators=[MaxLengthValidator(150), MinLengthValidator(4)])

	def __str__(self):
		retorno = (str(self.id_carrito) + " " + self.producto + " " + self.cliente)
		return retorno