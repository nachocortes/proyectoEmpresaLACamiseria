from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('add/<int:producto_id>/', views.cart_add, name='cartAdd'),
    path('remove/<int:producto_id>/', views.cart_remove, name='cartRemove'),
    path('create/', views.pedido_create, name='pedidoCreate'),
    path('pedidoDetail/<int:pk>/', views.PedidooDetailView.as_view(), name='pedido_detail'),
]
