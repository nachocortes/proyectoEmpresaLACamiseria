from django.shortcuts import render
from carts.views import obtener_o_crear_cart
from .models import Pedido
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def breadcrumb(productos=True, direccion=False, pago=False, confirmacion=False):
    return [

        {'titulo': 'Productos', 'activo': productos, 'url': reverse('pedidos:pedido')},
        {'titulo': 'Dirección', 'activo': direccion, 'url': reverse('pedidos:pedido')},
        {'titulo': 'Pago', 'activo': pago, 'url': reverse('pedidos:pedido')},
        {'titulo': 'Confirmación', 'activo': confirmacion, 'url': reverse('pedidos:pedido')}

    ]


@login_required(login_url='login')
def pedido(request):
    cart = obtener_o_crear_cart(request)
    pedido = cart.pedido
    if pedido is None and request.user.is_authenticated:
        pedido = Pedido.objects.create(cart=cart, user=request.user)
    if pedido:
        request.session['pedido_id'] = pedido.pedido_id
    print('Este es un carrito de un pedido', cart)
    return render(request, 'pedidos/pedido.html', {
        'cart': cart,
        'pedido': pedido,
        'breadcrumb': breadcrumb()
    })