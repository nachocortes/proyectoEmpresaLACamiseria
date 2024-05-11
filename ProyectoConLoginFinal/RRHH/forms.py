from django import forms
from RRHH.models import Departamento, Empleado, PuestoTrabajo


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'


class PuestoTrabajoForm(forms.ModelForm):
    class Meta:
        model = PuestoTrabajo
        fields = '__all__'
