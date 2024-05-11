import uuid
from enum import Enum
from django.db import models

from pedidos.choices import estado_choices
from users.models import User
from carts.models import Cart
from django.db.models.signals import pre_save


class Pedido(models.Model):
    pedido_id = models.CharField(max_length=100, null=False, blank=False, unique=True, primary_key=True,verbose_name='Pedido ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Carrito')
    estado = models.CharField(max_length=50, choices=estado_choices, verbose_name='Estado')
    compra_total = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Compra total')
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name='Total')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pedido_id

    def obtener_total(self):
        return self.cart.total + self.compra_total

    def actualizar_total(self):
        self.total = self.obtener_total()
        self.save()


def generar_pedido_id(sender, instance, *args, **kwargs):
    if not instance.pedido_id:
        instance.pedido_id = str(uuid.uuid4())


def generar_total(sender, instance, *args, **kwargs):
    instance.total = instance.obtener_total()

pre_save.connect(generar_pedido_id, sender=Pedido)
pre_save.connect(generar_total, sender=Pedido)