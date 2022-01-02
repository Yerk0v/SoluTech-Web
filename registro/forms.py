from django import forms

class FormularioRegistro(forms.Form): #Formulario para el registro de usuarios
    nombre_usuario = forms.CharField(max_length=50) #Nombre de usuario
    correo = forms.EmailField(label='Correo electrónico') #Campo para el correo
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput()) #Campo para la contraseña


