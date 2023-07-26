from django.shortcuts import render
from .forms import VehiculoForm
from .models import Vehiculo
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.


# Vista de la página inicio
def index(request):
    return render(request, 'index.html')

def add(request):
    """
    Vista del formulario con condicional
    Si entra a la pág mediante un método GET se crea una instancia vacía del formulario y 
    se renderiza para ingresar datos
    si se hace una petición POST verifica si el form es válido
    genera un objeto vehículo con los datos ingresados desde el
    formulario para guardarlos en la base de datos y finalmente redireccionar al inicio.
    """
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = Vehiculo.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
    else:
        form = VehiculoForm()
    return render(request, 'add.html',{'form': form})

@login_required
# Vista protegida para que la vea usuario logueado
def listar(request):
    """
    Vista de la tabla con el listado de vehículos
    Se accede a todos objetos vehículos de la BD y los almacena
    Se renderiza y se entregan los objetos como context para visualizarlos.
    """
    context = Vehiculo.objects.all()
    return render(request, 'listar.html', {'context' : context})