from django.shortcuts import render, redirect
from .models import Cita
from .forms import CitaForm
from django.contrib.auth.decorators import login_required


@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def citas(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        
        lista_citas = Cita.objects.filter(nombre_cliente__icontains=busqueda)
    else:
        lista_citas = Cita.objects.all()
        
    return render(request, 'citas/index.html', {'citas': lista_citas})
def crear(request):
    formulario = CitaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('citas')
    return render(request, 'citas/crear.html', {'formulario': formulario})

def editar(request, id):
    cita = Cita.objects.get(id=id)
    formulario = CitaForm(request.POST or None, request.FILES or None, instance=cita)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('citas')
    return render(request, 'citas/editar.html', {'formulario': formulario})

def eliminar(request, id):
    cita = Cita.objects.get(id=id)
    cita.delete()
    return redirect('citas')