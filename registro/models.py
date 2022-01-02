from django.db import models
from django.contrib.auth.models import User


class FormularioRegistro(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo = models.EmailField()
    password = models.CharField(max_length=50)



