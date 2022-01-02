from django.urls import path 

from . import views

urlpatterns = [
    path('',views.registro, name='Registrar'),
    path('inicio',views.inicio, name='Inicio'),
    path('log',views.Login, name='Login'),
]