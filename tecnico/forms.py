from django import forms

class registroTecnico(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=100)
    mensaje = forms.CharField(max_length=100)