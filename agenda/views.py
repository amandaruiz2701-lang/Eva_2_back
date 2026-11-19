from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm, RegistroClienteForm  # Importamos ambos formularios

def inicio(request):
    return render(request, 'paginas/inicio.html')


@login_required
def citas(request):
    busqueda = request.GET.get('buscar')
    
    if request.user.is_staff:
        lista_citas = Cita.objects.all()
        titulo = "Panel de Administración - Todas las Reservas 🛠️"
    else:
        lista_citas = Cita.objects.filter(cliente=request.user)
        titulo = "Mis Citas Agendadas 🌸"

    if busqueda and request.user.is_staff:
        lista_citas = lista_citas.filter(servicio__nombre__icontains=busqueda)
        
    return render(request, 'citas/index.html', {
        'citas': lista_citas,
        'titulo': titulo
    })

@login_required
def crear(request):
    formulario = CitaForm(request.POST or None, request.FILES or None)

    # Si no es admin, quitamos el campo 'cliente' del formulario para que no tenga que elegirlo
    if not request.user.is_staff and 'cliente' in formulario.fields:
        del formulario.fields['cliente']

    if request.method == 'POST' and formulario.is_valid():
        cita = formulario.save(commit=False)

        if not request.user.is_staff:
            cita.cliente = request.user
            cita.estado = 'Pendiente'
        else:
            if not cita.estado:
                cita.estado = 'Confirmada'

        cita.save()
        return redirect('citas')

    return render(request, 'citas/crear.html', {'formulario': formulario})
    
@login_required
def confirmar_cita(request, id):
    # Solo el staff (administrador del salón) puede confirmar citas
    if request.user.is_staff:
        cita = Cita.objects.get(id=id)
        cita.estado = 'Confirmada'
        cita.save()
    return redirect('citas')


    
@login_required
def confirmar_cita(request, id):
    # Solo el staff (administrador del salón) puede confirmar citas
    if request.user.is_staff:
        cita = Cita.objects.get(id=id)
        cita.estado = 'Confirmada'
        cita.save()
    return redirect('citas')

@login_required
def editar(request, id):
    cita = Cita.objects.get(id=id)
    formulario = CitaForm(request.POST or None, request.FILES or None, instance=cita)
    if request.method == 'POST' and formulario.is_valid():
        formulario.save()
        return redirect('citas')
    return render(request, 'citas/editar.html', {'formulario': formulario})

@login_required
def eliminar(request, id):
    cita = Cita.objects.get(id=id)
    cita.delete()
    return redirect('citas')

def registro(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('citas')  # Redirige a la página de citas después del registro
    else:
        form = RegistroClienteForm()
    return render(request, 'registration/registro.html', {'form': form})