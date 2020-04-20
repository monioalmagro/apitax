from django.urls import path, include
from django.contrib import admin
from core import views 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('',views.home, name='home'),
    path('ingreso/', include('ingreso.urls')),
    path('gasto/',include('ingreso.urls')),
    path('movimientos/',views.movimientos, name='movimientos'),
]

"""urlpatterns = [
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]"""