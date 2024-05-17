from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First Name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last Name')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email Address')}),
        }
        labels = {
            'username': 'Username',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                _("Esta dirección de correo electrónico ya está en uso. Proporcione una dirección de correo electrónico diferente."))
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(_("Este nombre de usuario ya está en uso. Por favor, elija otro."))
        return username


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        labels = {
            'username': 'Username',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Direccion de correo electronico',
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        common_attrs = {'class': 'form-control', 'label': '', 'placeholder': ''}
        placeholders = {
            'username': 'Username',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirma password'
        }
        for field_name, field in self.fields.items():
            field.widget.attrs.update(common_attrs)
            field.widget.attrs['placeholder'] = placeholders.get(field_name, field.widget.attrs.get('placeholder', ''))
            field.help_text = ''
