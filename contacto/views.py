from django.shortcuts import render, HttpResponse 
from contacto.models import Contacto

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        return render(request, 'contacto/mensaje.html')
    return render(request, 'contacto/contacto.html')








