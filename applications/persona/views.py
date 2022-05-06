from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
# models
from .models import Empleado
# forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    template_name = "incio.html"


class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 6
    

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave 
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    """ listar empleados de un area"""
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        #con esto se recole el parametro de la url
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
            departamento__short_name = area 
        )
        return lista

class ListEmpleadosByKword(ListView):
    """ Lista Empleado por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('**************************')
        palabra_clave = self.request.GET.get("kword",'')
        lista = Empleado.objects.filter(
            first_name = palabra_clave 
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado =  Empleado.objects.get(id=2)
        
        return empleado.habilidades.all()


#Modelos DetailView

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

# Class CreateView


class SuccesView(TemplateView):
    template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_all') 

    def form_valid(self, form):
        #Logica del proceso
        #Si se agrega l commit false, solo se crea la instancia para prepaprar los datos y despues guardar
        print('=========CREANDO REGISTRO===========')
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*************METODO POST***************')
        print('====================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('*************METODO Form Valid***************')
        print('****************************')
        return super().form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')


    #Por default    
    #model = Empleado
    #queryset = Empleado.objects.filter(
    #    departamento__short_name = 'Otro'
    #)

    
# 1.- Lista todos los empleados de la empresa
# 2.- Listar todos los empleados que perteneceen a una area de la empresa
# 3.- Listar empleados por trabajo
# 4.- Listar los empleados por palabra clave
# 5.- Listar habilidades de un empleado
