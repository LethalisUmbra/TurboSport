from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
# Models
from django.db.models import Sum
from django.contrib.auth.models import User
from .models import Carrito
# Forms
from django import forms

# HOME
@login_required
def HomeCarrito(request):
	try:
		carritos = Carrito.objects.filter(cliente=request.user.username).order_by('id_carrito')
		precio_total = sum(producto.precio for producto in carritos)
	except:
		return redirect('home')
	return render(request, 'carrito/home_carrito.html', {'carritos':carritos, 'precio_total':precio_total})

@login_required
def Eliminar(request):
	Carrito.objects.filter(cliente=request.user.username).delete()
	messages.success(request, 'Tu carrito ha sido eliminado con éxito')
	return HttpResponseRedirect('/')

@login_required
def QuitarProducto(request, id_carrito):
	Carrito.objects.get(id_carrito=id_carrito).delete()
	messages.success(request, 'Tu producto ha sido removido con éxito')
	return redirect('homeCarrito')

@login_required
def Comprar(request):
	# Por razones obvias no se hará la api para la compra
	# Ya que este código ha sido creado con un ámbito académico
	# Para simular una compra, se ha decidido quitar los productos del carro
	# Y dar un mensaje de éxito de compra.
	Carrito.objects.filter(cliente=request.user.username).delete()
	messages.success(request, 'La compra se ha realizado con éxito, los productos serán recibidos dentro de las siguientes 72 horas')
	return redirect('homeCarrito')