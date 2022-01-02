from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Servicio, ServicioAdmin)
