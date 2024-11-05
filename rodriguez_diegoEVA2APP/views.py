from django.shortcuts import render # type: ignore

# Create your views here.
from django.shortcuts import redirect, render # type: ignore
from rodriguez_diegoEVA2APP.models import Django_Seminario
from rodriguez_diegoEVA2APP.forms import FormSeminario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listarInscripciones(request):
    seminarios = Django_Seminario.objects.all()
    data = {'semi' : seminarios}
    return render(request, 'ListaInscripciones.html',data)

def agregarInscripciones(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listarI/')
    
    data ={'formSem': form}
    return render(request, 'agregarInscripciones.html', data)

def eliminarInscripcion(request, id):
    semi = Django_Seminario.objects.get(id = id)
    semi.delete()
    return redirect('/listarI/')

def actualizarInscripcion(request, id):
    semi = Django_Seminario.objects.get(id=id)
    form = FormSeminario(instance=semi)
    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=semi)
        if form.is_valid():
            form.save()
        return redirect('/listarI/')
    
    data = {'formS': form}
    return render(request, 'actualizarInscripcion.html', data)

    


