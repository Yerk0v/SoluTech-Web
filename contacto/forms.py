from django import forms
from .models import Contacto
class Contacto(forms.Form): 
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea)

