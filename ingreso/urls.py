from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingreso, name="ingreso"),
    path('gasto', views.gasto, name="gasto"),
    path('movimiento', views.movimiento, name="movimiento"),
]