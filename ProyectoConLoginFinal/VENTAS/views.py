from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST

from STORE.models import Producto
from .models import Cart, CartProductos, Pedido


def obtener_o_crear_cart(request):
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')

    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = obtener_o_crear_cart(request)
        return render(request, 'carts/cart.html', {
            'cart': cart
        })


class AgregarProducto(LoginRequiredMixin, View):
    @method_decorator(require_POST)
    def post(self, request):
        cart = obtener_o_crear_cart(request)
        producto_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, pk=producto_id)
        cantidad = int(request.POST.get('cantidad', 1))
        cart_producto = CartProductos.objects.crear_actualizar_cantidad(cart=cart, product=producto, quantity=cantidad)

        return render(request, 'carts/add.html', {
            'cantidad': cantidad,
            'producto': producto,
            'cp': cart_producto
        })


class EliminarProducto(LoginRequiredMixin, View):
    @method_decorator(require_POST)
    def post(self, request):
        cart = obtener_o_crear_cart(request)
        producto = get_object_or_404(Producto, pk=request.POST.get('producto_id'))
        cart.productos.remove(producto)
        messages.success(request, "Producto eliminado del carrito.")
        return redirect('carts:cart')


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
