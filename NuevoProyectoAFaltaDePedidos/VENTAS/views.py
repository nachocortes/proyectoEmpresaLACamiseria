from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, DetailView
from STORE.models import Producto
from VENTAS.cart import Cart
from VENTAS.forms import AgregarCartProductoForm, CrearPedidoForm
from VENTAS.models import PedidoItem, Pedido
from VENTAS.utils import render_to_pdf


@require_POST
def cart_add(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = AgregarCartProductoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            producto=producto,
            cantidad=cd['cantidad'],
            anular_cantidad=cd['anular'],
        )
    return redirect('cart:cart')


@require_POST
def cart_remove(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remove(producto)
    return redirect('cart:cart')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['actualizar_cantidad_form'] = AgregarCartProductoForm(
            initial={'cantidad': item['cantidad'], 'anular': True}
        )
    return render(request, 'cart/cart.html', {'cart': cart})


def pedido_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CrearPedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            for item in cart:
                PedidoItem.objects.create(
                    pedido=pedido,
                    producto=item['producto'],
                    precio=item['precio'],
                    cantidad=item['cantidad'],
                )
            cart.clear()
            return render(
                request, 'pedidos/pedido/created_pedido.html', {'pedido': pedido, 'cart': cart}
            )
    else:
        form = CrearPedidoForm()
    return render(
        request,
        'pedidos/pedido/create_pedido.html',
        {'cart': cart, 'form': form},
    )


class PedidooDetailView(DetailView):
    model = Pedido

    template_name = 'pedidos/pedido/pedido_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pedido_items'] = self.object.items.all()
        return context


class PedidoPdf(TemplateView):
    def get(self, request, *args, **kwargs):
        pedido = Pedido.objects.all()
        productos = PedidoItem.objects.all()

        data = {
            'pedido': pedido,
            'productos': productos,
        }
        pdf = render_to_pdf('pedidos/producto/pedido_detail.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
