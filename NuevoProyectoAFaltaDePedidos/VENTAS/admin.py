from django.contrib import admin
from .models import PedidoItem, Pedido


class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    raw_id_fields = ['producto']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellidos', 'email', 'direccion', 'codigo_postal', 'ciudad', 'pais', 'created',
                    'updated', ]
    list_filter = ['pais', 'created', 'updated']
    inlines = [PedidoItemInline]
