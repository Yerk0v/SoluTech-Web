from django.urls import path 
from django.conf import settings 
from contacto import views 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contacto, name='Contacto'),
]
