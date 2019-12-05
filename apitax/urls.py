

from django.contrib import admin
from django.urls import path
from core import views as core_views
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('home/', core_views.home, name='home'),
]

