from django.urls import path
from .views import index, contacto, galeria
urlpatterns = [
    path('', index, name = "index"),
    path('contacto/', contacto, name = "contacto"),
    path('galeria/', galeria, name = "galeria"),
    
]
