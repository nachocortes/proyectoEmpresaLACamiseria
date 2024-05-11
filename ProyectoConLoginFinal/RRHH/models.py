from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


class Departamento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    telefono = models.IntegerField(blank=True, null=True, verbose_name='Telefono')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
                                    verbose_name='Responsable departamento')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "departamento"
        verbose_name_plural = "departamentos"
        ordering = ["-created"]


class PuestoTrabajo(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name="Departamento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "Puesto de trabajo"
        verbose_name_plural = "Puestos de trabajos"
        ordering = ["-created"]


class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    # empleado = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'group__name': 'empleados'} , verbose_name="Empleado")
    puestoTrabajo = models.ForeignKey(PuestoTrabajo, on_delete=models.CASCADE, verbose_name="Puesto")
    dni = models.CharField(max_length=40, blank=True, null=True, verbose_name="DNI")
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.CharField(max_length=100, blank=True, null=True, verbose_name="Dirección")
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name="Email")
    fecha_nacimiento = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    imagen = models.ImageField(upload_to="empleados/", blank=True, null=True, verbose_name="Imagen")
    antiguedad = models.IntegerField(default=0, blank=True, null=True, verbose_name="Antiguedad")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def imagen_tag(self):
        return mark_safe('<img src="%s" style="max-width: 40px; max-height: 60px;" />' % (self.imagen.url))

    def empleado(self):
        return f"{self.apellidos} {self.nombre} "

    imagen_tag.allow_tags = True
    imagen_tag.short_description = 'Imagen'

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        ordering = ["-created"]
