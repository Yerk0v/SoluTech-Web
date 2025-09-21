from django.shortcuts import render, redirect
from registro.models import FormularioRegistro
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def registro(request):
        if  request.method == 'POST':
            nombre_usuario = request.POST.get("txt")
            correo = request.POST.get("correo")
            contraseña = request.POST.get("contraseña")
            FormularioRegistro.objects.create(nombre_usuario=nombre_usuario,correo=correo,password=contraseña)
            return render(request,'registro/registrado.html')
        return render(request,'registro/registrar.html')

def inicio(request):
    return render(request,"ServicioTecnicoApp/inicio.html")

def Login(request):
        if request.method == 'POST':
            correo = request.POST.get('correo')
            password = request.POST.get('contraseña')
            try:
                user = FormularioRegistro.objects.get(correo=correo,password=password)
                return redirect('Inicio')
            except FormularioRegistro.DoesNotExist:
                messages.error(request, 'Usuario o contraseña incorrectos')
        return render(request, 'registro/registrar.html')

def Logout(request):
    logout(request)
    return redirect('Login')
