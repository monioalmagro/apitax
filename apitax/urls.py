

from django.contrib import admin
from django.urls import path
from core import views 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.home, name='home'),
    path('ingreso/',views.ingreso, name='ingreso'),
    path('gastos/',views.gastos, name='gastos'),
    path('movimientos/',views.movimientos, name='movimientos'),
]

