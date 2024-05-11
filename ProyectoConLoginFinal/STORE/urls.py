from django.urls import path
from . import views
from .views import ProductoListView

app_name = 'store'

urlpatterns = [
    path('', ProductoListView.as_view(), name="index"),
    path('search', views.ProductoSearchListView.as_view(), name="search"),
    path('<slug:slug>', views.ProductoDetailView.as_view(), name="producto"),

]
