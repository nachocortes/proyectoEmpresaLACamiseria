from django.contrib import admin
from .models import Departamento, PuestoTrabajo, Empleado


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'telefono', 'responsable', 'id')
    ordering = ('nombre', 'id')
    search_fields = ('nombre', 'telefono')
    list_display_links = ('nombre',)
    list_filter = ('nombre',)
    list_per_page = 8


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('apellidos',)
    list_display = ('imagen_tag', 'empleado', 'dni', 'email', 'departamento', 'puestoTrabajo', 'id')
    search_fields = ('apellidos', 'dni', 'email')
    list_display_links = ('empleado',)
    list_filter = ('departamento', 'puestoTrabajo')
    list_per_page = 8


@admin.register(PuestoTrabajo)
class PuestoTrabajoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'departamento')
    ordering = ('departamento', 'nombre')
    search_fields = ('nombre',)
    list_display_links = ('nombre',)
    list_filter = ('nombre',)
    list_per_page = 8
