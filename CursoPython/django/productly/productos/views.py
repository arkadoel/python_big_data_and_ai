from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Producto

# Create your views here.

#def index(request):
#    return HttpResponse('hola mundo')

def index(request):
    productos = Producto.objects.all().values() # todos
    print(productos)
    # FILTER
    # puntaje = 3
    # puntaje__gte = 3 #mayor o igual
    # puntaje__lte = 3 #menor o igual
    # puntaje__gt = 3 #mayor que
    # puntaje__lt = 3 #menor que
    # productos = Producto.objects.filter(puntaje=3)

    # UN ELEMENTO EN ESPECIFICO
    #productos = Producto.objects.get(id=1)

    return JsonResponse(list(productos), safe=False) #si no ponemos safe= dara un error


