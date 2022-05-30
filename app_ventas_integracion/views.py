from django.shortcuts import render

# Create your views here.

def index (request): # encuentra el html
    return render(request, 'app_ventas_integracion/index.html')

def contacto (request): # encuentra el html
    return render(request, 'app_ventas_integracion/contacto.html')

def galeria (request): # encuentra el html
    return render(request, 'app_ventas_integracion/galeria.html')


