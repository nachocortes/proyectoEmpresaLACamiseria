from django.contrib import admin
from django.template.defaulttags import url
from django.utils.html import format_html
from store.models import GaleriaProductos, Variante, Noticia
from store.models import Categoria, Producto

class GaleriaProductoInLine(admin.TabularInline):
    model = GaleriaProductos
    extra = 1

@admin.register(Categoria)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre','slug', 'precio', 'stock', 'categoria', 'disponibilidad', 'imagen_tag')
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [GaleriaProductoInLine]
    list_filter = ['nombre','disponibilidad','categoria']
    list_editable = ['precio', 'stock', 'disponibilidad']
    search_fields = ['nombre']
    list_display_links = ['nombre']
    ordering = ['nombre', 'id']
    list_per_page = 10

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo']


class VarianteAdmin(admin.ModelAdmin):
    list_display = ('producto', 'categoria_variante', 'valor', 'activo')
    list_editable = ('activo',)
    list_filter = ('producto', 'categoria_variante', 'valor', 'activo')



#admin.site.register(AddOpnion)

admin.site.register(GaleriaProductos)
admin.site.register(Variante, VarianteAdmin)

