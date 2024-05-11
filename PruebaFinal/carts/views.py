from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST

from store.models import Producto
from .models import Cart, CartProductos

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