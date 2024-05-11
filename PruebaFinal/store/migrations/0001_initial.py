# Generated by Django 5.0.6 on 2024-05-11 01:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GaleriaProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='store/productos/galeria/%Y/%m/%d', verbose_name='Imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, unique=True, verbose_name='Titulo')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('contenido', models.TextField(blank=True, max_length=255, null=True, verbose_name='Contenido')),
                ('fecha_publicacion', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Fecha publicacion')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
                'ordering': ['fecha_publicacion'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('imagen', models.ImageField(default='img/product_default.png', upload_to='img/productos/%Y/%m/%d', verbose_name='Imagen')),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('color', models.CharField(blank=True, max_length=100, null=True, verbose_name='Color')),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='precio')),
                ('stock', models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Stock')),
                ('disponibilidad', models.BooleanField(default=True, verbose_name='Disponibilidad')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Variante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria_variante', models.CharField(choices=[('color', 'color'), ('talla', 'talla')], max_length=100, verbose_name='Categoria variante')),
                ('valor', models.CharField(max_length=100, verbose_name='Valor')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ['nombre'],
                'indexes': [models.Index(fields=['nombre'], name='store_categ_nombre_e8fa22_idx')],
            },
        ),
    ]
