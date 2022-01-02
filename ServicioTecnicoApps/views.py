from django.shortcuts import render, HttpResponse 
from servicios.models import Servicio


def inicio(request):
    return  render(request,"ServicioTecnicoApp/inicio.html")

def tienda(request):
    return  render(request,"ServicioTecnicoApp/tienda.html")


