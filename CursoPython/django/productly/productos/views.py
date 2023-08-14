from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from .models import Producto
from .forms import ProductoForm

# Create your views here.
"""
def index(request):
    return HttpResponse('hola mundo')
"""

"""
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
"""

def index(request):
    productos = Producto.objects.all()
    
    return render(
        request,
        'index.html',
        context={'productos' : productos}
    )

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    return render(request, 'detalle.html', context={'producto': producto})
    
def formulario(request):

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )