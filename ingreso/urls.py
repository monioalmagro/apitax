from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingreso, name="ingreso"),
    path('gasto', views.gasto, name="gasto"),
    path('movimientos', views.movimientos, name="movimientos"),
]