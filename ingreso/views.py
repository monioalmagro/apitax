from django.shortcuts import render, get_object_or_404,redirect
from .models import Ingreso,Cuenta, Movimiento
from .forms import IngresoForm


# Create your views here.

def ingreso(request):
    ingreso = Ingreso.objects.all()
    return render(request, "ingreso/ingreso.html", {'ingreso':ingreso})

def gasto(request):
    cuenta = Cuenta.objects.all()
    return render(request,"ingreso/gasto.html", {'cuenta':cuenta})  

def movimiento(request):      
    movimiento = Movimiento.objects.all()
    return render(request,"ingreso/movimiento.html", {'movimiento':movimiento})

def new(request):
    form = IngresoForm
    return render(request,"ingreso/formulario.html",{'form':form})

def new(request):
    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.author = request.user
            #ingreso.published_date = timezone.now()
            ingreso.save()
            return redirect('movimiento')
    else:
        form = IngresoForm()
    return render(request, 'ingreso/formulario.html', {'form': form})