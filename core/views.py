from django.shortcuts import render


def home(request):
    return render(request, "core/home.html" )

#def ingreso(request):
#	return render(request,"core/ingreso.html")     

#def gastos(request):
#	return render(request,"core/gastos.html")	

#def movimientos(request):
#	return render(request,"core/movimientos.html")		

