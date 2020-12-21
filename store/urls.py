from django.urls import path
from . import views

#Login / logout
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.products, name='home'),
    path('productos/categoria/<str:categoria>', views.filtrarCategoria, name='filtrarCategoria'),
    path('productos/tipo/<str:tipo_producto>', views.filtrarTipoProducto, name='filtrarTipoProducto'),
    path('productos/marca/<str:marca>', views.filtrarMarca, name='filtrarMarca'),
    path('productos/talla/<str:talla>', views.filtrarTalla, name='filtrarTalla'),
    path('productos/color/<str:color>', views.filtrarColor, name='filtrarColor'),
    path('logout', LogoutView.as_view(template_name='store/listado.html'), name='logout'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('delete', views.deleteUser, name='deleteUser'),
    path('productos/<int:id_producto>', views.detalleProducto, name='producto'),
    path('productos/comprar/<int:id_producto>', views.ComprarProducto, name='comprarProducto')
]
