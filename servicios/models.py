from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return self.nombre
        
