sterfrom django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.urls import reverse

# Formulario y Autenticación del Usuario
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

#Models
from .models import Producto
from carrito.models import Carrito
from .forms import UCFCompleted, UpdateUser

# Create your views here.
def home(request):
	login(request)
	categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
	return render(request, 'store/home.html', {'categories':categories})

def products(request):
	# Se llaman todos los productos para luego ser listados
	products = Producto.objects.all().order_by('nombre')

	# LISTADO FILTRO
	categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
	product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
	brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
	size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
	colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

	context = {
		'products': products,
		'categories': categories,
		'product_type': product_type,
		'brand': brand,
		'size': size,
		'colour': colour
	}

	login(request)

	return render(request, 'store/listado.html', context)

def register(request):
	login(request)
	register_form = UCFCompleted()
	# codigo para el formulario del registro
	if request.method == "POST" and 'register_btn':
		register_form = UCFCompleted(request.POST)
		if register_form.is_valid():
			register_form.save();
			return HttpResponseRedirect('/')

	return render(request, 'store/registro.html', {'registro': register_form})

def login(request):
	# codigo para el formulario del login con autenticación
	login_form = AuthenticationForm()
	if request.method == "POST" and 'login_btn':
		login_form = AuthenticationForm(data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request, user)
				return redirect('home')

@login_required
def profile(request):
	login(request)
	obj= get_object_or_404(User, username=request.user.username)
	update_form = UpdateUser(request.POST or None, instance=obj)
	if request.method == "POST" and 'update_btn':
		if update_form.is_valid():
			obj=update_form.save(commit = False)
			obj.save()
			return	render(request, 'store/profile.html', {'update': update_form})

	return render(request, 'store/profile.html', {'update': update_form})

@login_required
def deleteUser(request):
	try:
		u = User.objects.get(username= request.user.username)
		u.delete()
		return redirect('home')
	except User.DoesNotExist:
		return render(request, 'store/home.html')
	return render(request, 'store/home.html')

def detalleProducto(request, id_producto):
	login(request)
	p = get_object_or_404(Producto, id_producto=id_producto)
	return render(request, 'store/producto.html', {'producto':p})


# VISTAS PARA LOS FILTROS

def filtrarCategoria(request, categoria):
	login(request)
	products = Producto.objects.filter(categoria=categoria).order_by('nombre')

	if products is not None:
			# LISTADO FILTRO
		categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
		product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
		brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
		size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
		colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

		context = {
			'products': products,
			'categories': categories,
			'product_type': product_type,
			'brand': brand,
			'size': size,
			'colour': colour
		}

		return render(request, 'store/listado.html', context)

	else:
		return redirect('products')

	return render(request, 'store/listado.html', {'products':products})

def filtrarTipoProducto(request, tipo_producto):
	login(request)
	products = Producto.objects.filter(tipo_producto=tipo_producto).order_by('nombre')

	if products is not None:
			# LISTADO FILTRO
		categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
		product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
		brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
		size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
		colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

		context = {
			'products': products,
			'categories': categories,
			'product_type': product_type,
			'brand': brand,
			'size': size,
			'colour': colour
		}

		return render(request, 'store/listado.html', context)

	else:
		return redirect('products')

	return render(request, 'store/listado.html', {'products':products})

def filtrarMarca(request, marca):
	login(request)
	products = Producto.objects.filter(marca=marca).order_by('nombre')

	if products is not None:
			# LISTADO FILTRO
		categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
		product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
		brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
		size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
		colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

		context = {
			'products': products,
			'categories': categories,
			'product_type': product_type,
			'brand': brand,
			'size': size,
			'colour': colour
		}

		return render(request, 'store/listado.html', context)

	else:
		return redirect('products')

	return render(request, 'store/listado.html', {'products':products})

def filtrarTalla(request, talla):
	login(request)
	products = Producto.objects.filter(talla=talla).order_by('nombre')

	if products is not None:
			# LISTADO FILTRO
		categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
		product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
		brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
		size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
		colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

		context = {
			'products': products,
			'categories': categories,
			'product_type': product_type,
			'brand': brand,
			'size': size,
			'colour': colour
		}

		return render(request, 'store/listado.html', context)

	else:
		return redirect('products')

	return render(request, 'store/listado.html', {'products':products})

def filtrarColor(request, color):
	login(request)
	products = Producto.objects.filter(color=color).order_by('nombre')

	if products is not None:
			# LISTADO FILTRO
		categories = Producto.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
		product_type = Producto.objects.values_list('tipo_producto', flat=True).distinct().order_by('tipo_producto')
		brand = Producto.objects.values_list('marca', flat=True).distinct().order_by('marca')
		size = Producto.objects.values_list('talla', flat=True).distinct().order_by('talla')
		colour = Producto.objects.values_list('color', flat=True).distinct().order_by('color')

		context = {
			'products': products,
			'categories': categories,
			'product_type': product_type,
			'brand': brand,
			'size': size,
			'colour': colour
		}

		return render(request, 'store/listado.html', context)

	else:
		return redirect('products')

	return render(request, 'store/listado.html', {'products':products})

@login_required
def ComprarProducto(request, id_producto):
	instance = Carrito()
	instance.producto = Producto.objects.get(id_producto=id_producto).nombre
	instance.precio = Producto.objects.get(id_producto=id_producto).precio
	instance.cliente = request.user.username
	instance.save()
	messages.success(request, 'Tu producto ha sido agregado con éxito al carrito')
	return redirect('homeCarrito')