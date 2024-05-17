from django.contrib import admin
from django.utils.html import format_html
from CRM.models import Direccion, Cliente
from RRHH.models import Empleado


class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1


class ComercialTecGestionFilter(admin.SimpleListFilter):
    title = ('Comercial')
    parameter_name = 'comercial'

    def lookups(self, request, model_admin):
        empleados = Empleado.objects.filter(puestoTrabajo__nombre='TecGestionComercial')
        return [(e.id, e.nombre) for e in empleados]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(comercial__id=self.value())


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'listar_direcciones')
    inlines = [DireccionInline]
    list_filter = ('tipoCliente', ComercialTecGestionFilter)
    search_fields = ('nombre', 'documento', 'email', 'telefono')
    readonly_fields = ('created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('nombre', 'tipoDocumento', 'documento')
        }),
        ('Información de Contacto', {
            'fields': ('email', 'telefono', 'comercial', 'tipoCliente')
        }),
        ('Metadata', {
            'fields': ('created', 'updated'),
            'classes': ('collapse',)
        }),
    )

    def listar_direcciones(self, obj):
        direcciones = obj.direcciones.all()
        return format_html("<br>".join([f"{d.tipoDireccion}: {d.ciudad}, {d.pais}" for d in direcciones]))

    listar_direcciones.short_description = "Direcciones"


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'tipoDireccion', 'tipoVia', 'calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    list_filter = ('tipoDireccion', 'pais', 'ciudad')
    search_fields = ('calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    readonly_fields = ('created', 'updated')
    list_per_page = 8
