from django.urls import path, include
from django.contrib import admin
from core import views 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.home, name='home'),
    path('ingreso/', include('ingreso.urls')),
    
]

