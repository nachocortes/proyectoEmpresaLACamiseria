from django.urls import path
from . import views
from .views import ProductoListView

app_name = 'store'

urlpatterns = [
    path('', views.home_store, name="home_store"),
    path('prueba', views.prueba, name="puebra"),
    path('productos', ProductoListView.as_view(), name="index"),
    path('search', views.ProductoSearchListView.as_view(), name="search"),
    path('<slug:slug>', views.ProductoDetailView.as_view(), name="producto"),

]
