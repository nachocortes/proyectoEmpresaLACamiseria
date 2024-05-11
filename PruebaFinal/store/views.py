from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Producto
from django.views.generic.detail import DetailView
from django.db.models import Q

class ProductoListView(ListView):
    template_name = 'index.html'
    queryset = Producto.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        print(context)
        context['productos'] = context['producto_list']
        return context


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductoSearchListView(ListView):
    template_name = 'productos/search.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(categoria__nombre__icontains=self.query())
        return Producto.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['producto_list'].count()
        print('Este es query', context['query'])
        return context