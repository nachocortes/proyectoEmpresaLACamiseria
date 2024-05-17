from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.inicio_store, name="inicioStore"),
    path('productos/', views.productos_store, name="productosStore"),
    path('about/', views.about_store, name="aboutStore"),
    path('blog/', views.blog_store, name="blogStore"),
    path('contacto/', views.contacto_store, name="contactoStore"),
    path('productolist/', views.producto_list, name='productoList'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='productoDetail'),
    path('search', views.ProductoSearchListView.as_view(), name="search"),
]
