from django.shortcuts import render, get_object_or_404
from .models import Ingreso,Cuenta, Movimiento

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