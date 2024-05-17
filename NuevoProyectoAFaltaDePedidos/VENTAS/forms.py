from django import forms
from .models import Pedido

producto_cantidad_choices = [(i, str(i)) for i in range(1, 21)]


class AgregarCartProductoForm(forms.Form):
    cantidad = forms.TypedChoiceField(choices=producto_cantidad_choices, coerce=int)
    anular = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CrearPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre', 'apellidos', 'email', 'direccion', 'codigo_postal', 'ciudad', ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nombre"}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            # 'telefono': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo postal'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            # 'provincia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provincia'}),
            # 'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pais'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'email': 'Direccion de correo electronico',
            # 'telefono': 'Telefono',
            'direccion': 'Direccion',
            'codigo_postal': 'Codigo postal',
            'ciudad': 'Ciudad',
            # 'provincia': 'Provincia',
            # 'pais': 'Pais',
        }
