from django.shortcuts import render, get_object_or_404
from .models import Ingreso

# Create your views here.

def ingreso(request):
    ingreso = Ingreso.objects.all()
    return render(request, "ingreso/ingreso.html", {'ingreso':ingreso})

def gasto(request):
    gasto = Ingreso.objects.all()
    return render(recuest,"ingreso/gasto.html",{'ingreso':ingreso})    