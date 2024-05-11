from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe

from users.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    descripcion = models.TextField(max_length=255, blank=True, null=True, verbose_name='Descripcion')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['nombre']),
        ]

    def __str__(self):
        return self.nombre

    def get_url(self):
        return reverse('store:productos_by_categoria', args=[self.slug])


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,
                                  related_name='productos', verbose_name='Categoria')
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    imagen = models.ImageField(upload_to='img/productos/%Y/%m/%d', default='img/product_default.png',
                               verbose_name='Imagen')
    descripcion = models.TextField(max_length=255, null=True, blank=True, verbose_name='Descripcion')
    color = models.CharField(max_length=100, null=True, blank=True, verbose_name="Color")
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True,
                                 verbose_name='precio')
    stock = models.PositiveIntegerField(default=1, null=True, blank=True, verbose_name='Stock')
    disponibilidad = models.BooleanField(default=True, verbose_name='Disponibilidad')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['nombre']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.nombre

    def get_url(self):
        return reverse('store:producto_detail', args=[self.categoria.slug, self.slug])

    def imagen_tag(self ):
            return mark_safe('<img src="%s" style="max-width: 40px; max-height: 60px;" />'% (self.imagen.url))


class GaleriaProductos(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None, related_name='imagenes',
                                 verbose_name='Producto')
    imagen = models.ImageField(upload_to='store/productos/galeria/%Y/%m/%d', blank=True, null=True,
                               verbose_name='Imagen')

    def __str__(self):
        return self.producto.nombre


class AdministrarVariantes(models.Manager):
    def colores(self):
        return super(AdministrarVariantes, self).filter(variante='color', activo=True)

    def tallas(self):
        return super(AdministrarVariantes, self).filter(variante='talla', activo=True)


categoria_variante_choice = (
    ('color', 'color'),
    ('talla', 'talla'),
)


class Variante(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variantes', verbose_name='Producto')
    categoria_variante = models.CharField(max_length=100, choices=categoria_variante_choice,
                                          verbose_name='Categoria variante')
    valor = models.CharField(max_length=100, verbose_name='Valor')
    activo = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AdministrarVariantes()

    def __str__(self):
        return self.categoria_variante + ' : ' + self.valor


class Noticia(models.Model):
    titulo = models.CharField(max_length=200, unique=True, verbose_name='Titulo')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='Slug')
    contenido = models.TextField(max_length=255, blank=True, null=True, verbose_name='Contenido')
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Autor')
    fecha_publicacion = models.DateField(default=timezone.now, null=True, blank=True, verbose_name='Fecha publicacion')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'
        ordering = ['fecha_publicacion']
