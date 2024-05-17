from decimal import Decimal
from django.conf import settings
from STORE.models import Producto


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        producto_id = self.cart.keys()
        productos = Producto.objects.filter(id__in=producto_id)
        cart = self.cart.copy()
        for producto in productos:
            cart[str(producto.id)]['producto'] = producto
        for item in cart.values():
            item['precio'] = Decimal(item['precio'])
            item['total_precio'] = item['precio'] * item['cantidad']
            yield item

    def __len__(self):
        return sum(item['cantidad'] for item in self.cart.values())

    def add(self, producto, cantidad=1, anular_cantidad=False):
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {
                'cantidad': 0,
                'precio': str(producto.precio),
            }
        if anular_cantidad:
            self.cart[producto_id]['cantidad'] = cantidad
        else:
            self.cart[producto_id]['cantidad'] += cantidad
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def obtener_total_precio(self):
        return sum(
            Decimal(item['precio']) * item['cantidad']
            for item in self.cart.values())
