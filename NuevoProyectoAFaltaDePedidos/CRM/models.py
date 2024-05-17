from django.db import models
from CRM.choices import tipo_documento_choices, tipo_cliente_choices, tipo_direccion_choices, tipo_via_choices
from RRHH.models import Empleado


class Cliente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Cliente")
    # user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='clientes_registro',limit_choices_to={'groups__name': 'clientes'},verbose_name="Cliente")
    tipoDocumento = models.CharField(max_length=20, null=True, verbose_name="Tipo de Documento",
                                     choices=tipo_documento_choices)
    documento = models.CharField(max_length=60, verbose_name="Documento del Cliente")
    comercial = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, verbose_name="Comercial Asignado")
    password = models.CharField(max_length=50, unique=True, verbose_name="Contraseña del Cliente")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    telefono = models.PositiveIntegerField(blank=True, null=True, verbose_name="Teléfono")
    tipoCliente = models.CharField(max_length=200, blank=True, verbose_name="Tipo de Cliente",
                                   choices=tipo_cliente_choices)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre

    class Meta:
        # db_table = 'Clientes'
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
        ordering = ['id']


class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='direcciones', on_delete=models.CASCADE)
    tipoDireccion = models.CharField(max_length=200, null=True, verbose_name="Tipo de Direccion",
                                     choices=tipo_direccion_choices)
    tipoVia = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tipo de via",
                               choices=tipo_via_choices)
    calle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Calle")
    numero = models.CharField(max_length=50, blank=True, null=True, verbose_name="Numero piso letra")
    telefono = models.PositiveIntegerField(blank=True, null=True, verbose_name="Telefono")
    codigoPostal = models.PositiveIntegerField(blank=True, null=True, verbose_name="Codigo Postal")
    ciudad = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ciudad")
    pais = models.CharField(max_length=100, blank=True, null=True, verbose_name="País")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return f"{self.calle},{self.numero}"

    class Meta:
        # db_table = 'Direccion'
        verbose_name = "dirección"
        verbose_name_plural = "direcciones"
        ordering = ['tipoDireccion']
