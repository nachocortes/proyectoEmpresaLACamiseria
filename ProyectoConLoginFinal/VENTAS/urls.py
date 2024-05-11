from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart'),
    path('agregar', views.AgregarProducto.as_view(), name='agregar'),
    path('eliminar', views.EliminarProducto.as_view(), name='eliminar'),
    path('pedido/', views.pedido, name='pedido'),
]
