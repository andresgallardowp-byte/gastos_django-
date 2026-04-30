
from django.shortcuts import render, redirect
from .forms import GastoForm
from .models import Gasto


def inicio(request):

    lista_gastos = Gasto.objects.all().order_by('-fecha')
    

    return render(request, 'principal/inicio.html', {'gastos': lista_gastos})









def registrar_gasto(request):

    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('inicio') 
    
    # Si el usuario solo está entrando a la página para ver el formulario vacío
    else:
        form = GastoForm()
    
    # este es el formulario para registrar gastos de 'registrar_gasto.html'
    return render(request, 'principal/registrar.html', {'form': form})


def home(request):
    return render(request, 'principal/home.html')

def contacto(request):
    return render(request, 'principal/contacto.html')






from django.shortcuts import get_object_or_404

# esto es para la función para EDITAR
def editar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = GastoForm(instance=gasto)
    return render(request, 'principal/registrar.html', {'form': form, 'editando': True})

# y esto es para la función para ELIMINAR
def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    gasto.delete()
    return redirect('inicio')




# y esto otro es mostrar un mensaje de éxito al eliminar un gasto
from django.contrib import messages

def eliminar_gasto(request, id):
    gasto = get_object_or_404(Gasto, id=id)
    gasto.delete()
    messages.success(request, "Gasto eliminado correctamente.")
    return redirect('inicio')