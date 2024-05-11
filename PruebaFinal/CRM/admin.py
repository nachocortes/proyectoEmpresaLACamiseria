from django.contrib import admin
from django.utils.html import format_html
from CRM.models import Direccion, Cliente
from RRHH.models import Empleado


class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1

class ComercialTecGestionFilter(admin.SimpleListFilter):
    nombre = ('Comercial')
    nombre_buscado = 'comercial'

    def búsquedas(self, request, model_admin):
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


    def get_nombre_comercial(self, obj):
        if obj.comercial and obj.comercial.puestoTrabajo and obj.comercial.puestoTrabajo.nombre == 'TecGestionComercial':
            return obj.comercial.nombre
        return 'No Asignado'
    get_nombre_comercial.short_description = 'Nombre del Comercial'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "comercial":
            kwargs["queryset"] = Empleado.objects.filter(puestoTrabajo__nombre='TecGestionComercial')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    def listar_direcciones(self, obj):
        direcciones = obj.direcciones.all()
        return format_html("<br>".join([f"{d.tipoDireccion}: {d.ciudad}, {d.pais}" for d in direcciones]))

    listar_direcciones.short_description = "Direcciones"

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cliente','tipoDireccion', 'tipoVia', 'calle', 'numero','codigoPostal', 'ciudad', 'pais')
    list_filter = ('tipoDireccion', 'pais', 'ciudad')
    search_fields = ('calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    readonly_fields = ('created', 'updated')
    list_per_page = 8
