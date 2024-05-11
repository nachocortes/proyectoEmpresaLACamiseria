import decimal
import uuid
from django.db import models
from users.models import User
from store.models import Producto
from django.db.models.signals import pre_save, post_save, m2m_changed


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='Carrito')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Usuario')
    productos = models.ManyToManyField(Producto, through='CartProductos', verbose_name='Productos')
    subtotal = models.DecimalField(default=0.0, max_digits=10, decimal_places=2,verbose_name='Subtotal')
    total = models.DecimalField(default=0.0, max_digits=10, decimal_places=2,verbose_name='Total')
    created_at = models.DateTimeField(auto_now_add=True)

    FEE = 0.05  # comision del 5% de la compra

    def __str__(self):
        return self.cart_id

    def actualizar_totales(self):
        self.actualizar_subtotal()
        self.actualizar_total()

        if self.pedido:
            self.pedido.actualizar_total()

    def actualizar_subtotal(self):
        self.subtotal = sum([
            cp.cantidad * cp.producto.precio for cp in self.productos_relacionados()
        ])
        self.save()

    def actualizar_total(self):
        self.total = self.subtotal * decimal.Decimal(1 + Cart.FEE)
        self.save()

    def productos_relacionados(self):
        return self.cartproductos_set.select_related('producto')

    @property
    def pedido(self):
        return self.pedido_set.first()


class CartProductosManager(models.Manager):

    def crear_actualizar_cantidad(self, cart, producto, cantidad=1):
        object, creado = self.obtener_o_crear(cart=cart, producto=producto)

        if not creado:
            cantidad = object.cantidad + cantidad
        object.actualizar_cantidad(cantidad)
        return object


class CartProductos(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='carrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='producto')
    cantidad = models.IntegerField(default=1, verbose_name='cantidad')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CartProductosManager()

    def actualizar_cantidad(self, cantidad=1):
        self.cantidad = cantidad
        self.save()


def generar_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())


def actualizar_totales(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.actualizar_totales()


def enviar_guardar_actualizar_totales(sender, instance, *args, **kwargs):
    instance.cart.actualizar_totales()


# callbacks
pre_save.connect(generar_cart_id, sender=Cart)
post_save.connect(enviar_guardar_actualizar_totales, sender=CartProductos)
m2m_changed.connect(actualizar_totales, sender=Cart.productos.through)