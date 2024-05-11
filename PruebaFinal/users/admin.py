from django.contrib import admin
from .models import User, Customer, Perfil
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Perfil)