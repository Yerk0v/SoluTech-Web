from django.db import models
from django import forms

class registroTecnico(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre