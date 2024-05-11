from django.contrib import admin
from django.utils.html import format_html
from CRM.models import Direccion, Cliente
from RRHH.models import Empleado


class DireccionInline(admin.TabularInline):
    model = Direccion
    extra = 1


class ComercialTecGestionFilter(admin.SimpleListFilter):
    title = ('Comercial')  # Título del filtro en el panel de administración
    parameter_name = 'comercial'  # Parámetro que se usará en la URL para el filtro

    def lookups(self, request, model_admin):
        """
        Retorna la lista de empleados que tienen el puesto 'TecGestionComercial'.
        Cada tupla contiene el ID del empleado y su nombre, mostrado en la interfaz.
        """
        empleados = Empleado.objects.filter(puestoTrabajo__nombre='TecGestionComercial')
        return [(e.id, e.nombre) for e in empleados]

    def queryset(self, request, queryset):
        """
        Retorna el queryset modificado basado en el empleado seleccionado por el usuario.
        """
        if self.value():
            return queryset.filter(comercial__id=self.value())  # Filtra clientes por el empleado seleccionado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'listar_direcciones')
    inlines = [DireccionInline]
    list_filter = ('tipoCliente', ComercialTecGestionFilter)  # Use the custom filter class here
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
        """
        Este método recupera todas las direcciones asociadas con un cliente
        y las devuelve formateadas para mostrar en el panel de administración.
        """
        direcciones = obj.direcciones.all()  # Usamos related_name='direcciones' definido en el modelo Direccion
        return format_html("<br>".join([f"{d.tipoDireccion}: {d.ciudad}, {d.pais}" for d in direcciones]))

    listar_direcciones.short_description = "Direcciones"

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cliente','tipoDireccion', 'tipoVia', 'calle', 'numero','codigoPostal', 'ciudad', 'pais')
    list_filter = ('tipoDireccion', 'pais', 'ciudad')
    search_fields = ('calle', 'numero', 'codigoPostal', 'ciudad', 'pais')
    readonly_fields = ('created', 'updated')
    list_per_page = 8










