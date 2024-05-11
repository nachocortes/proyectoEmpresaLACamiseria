from django.views import View
from django.views.generic import DetailView, ListView
from RRHH.models import Departamento, Empleado, PuestoTrabajo


class DepartamentoListView(ListView):
    model = Departamento


class DepartamentoDetailView(DetailView):
    model = Departamento


class DepartamentoCreateView(View):
    model = Departamento


class EmpleadoListView(ListView):
    model = Empleado


class EmpleadoDetailView(DetailView):
    model = Empleado


class EmpleadoCreateView(View):
    model = Empleado


class HabilidadView(DetailView):
    model = PuestoTrabajo


class PuestotrabjaDetailView(DetailView):
    model = PuestoTrabajo


class PuestoTrabajoCreateView(View):
    model = PuestoTrabajo
