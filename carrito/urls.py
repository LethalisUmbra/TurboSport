from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.HomeCarrito, name='homeCarrito'),
	path('comprar', views.Comprar, name='comprar'),
	path('eliminar', views.Eliminar, name='eliminar'),
	path('quitar/<int:id_carrito>', views.QuitarProducto, name='quitarProducto')
]