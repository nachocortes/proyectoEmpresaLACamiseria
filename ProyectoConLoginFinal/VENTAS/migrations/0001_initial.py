# Generated by Django 5.0.6 on 2024-05-11 18:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('STORE', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=100, unique=True, verbose_name='Carrito')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Subtotal')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Total')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='CartProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1, verbose_name='cantidad')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VENTAS.cart', verbose_name='carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='STORE.producto', verbose_name='producto')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='productos',
            field=models.ManyToManyField(through='VENTAS.CartProductos', to='STORE.producto', verbose_name='Productos'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('pedido_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Pedido ID')),
                ('estado', models.CharField(choices=[('CREADO', 'CREADO'), ('PREPARANDO', 'PREPARANDO'), ('COMPLETADO', 'COMPLETADO'), ('ENVIADO', 'ENVIADO'), ('ENTREGADO', 'ENTREGADO'), ('DEVUELTO', 'DEVUELTO'), ('RECEPCIONADO', 'RECEPCIONADO'), ('PAGADO', 'PAGADO'), ('CANCELADO', 'CANCELADO')], max_length=50, verbose_name='Estado')),
                ('compra_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Compra total')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Total')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VENTAS.cart', verbose_name='Carrito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]