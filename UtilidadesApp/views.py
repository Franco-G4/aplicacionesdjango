from django.http import response
from django.shortcuts import *
from UtilidadesApp.models import abonados

def home(request):
    return render(request, 'UtilidadesApp/home.html')

def pares(request):
    Abonados = abonados.objects.all() #ver error
    return render(request, 'UtilidadesApp/parestelefonicos.html', {"abonados": Abonados})
    
    


