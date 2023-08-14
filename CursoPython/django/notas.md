# django

Instalar 
```bash
pipenv install django==4.1.7
pipenv shell
pipenv graph #asegurarse que tenemos django 4
django-admin startproject productly . #el punto final es para que lo haga en la carpeta actual

```

para ejecutar el sitio creado damos a 
```bash
python3 manage.py runserver
```

sale esto en la consola
```bash
(productly) nuc@NUC7CJYH:/media/WD/PROYECTOS/2023/python_big_data_and_ai/python_big_data_and_ai/CursoPython/django/productly$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 09, 2023 - 14:11:10
Django version 4.1.7, using settings 'productly.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[09/Aug/2023 14:11:16] "GET / HTTP/1.1" 200 10681
```
vemos como tenemos django 4.1.7

Un proyecto django pueden contener multiples aplicaciones

# creando una aplicacion

```bash
python3 manage.py startapp productos
```
Ahora instalamos la applicacion dentro del proyecto.
tomamos el nombre de la clase dentro del archivo productly/productos/app.py y editamos el archivo productly/settings.py en INSTALLED_APPS, lo añadimos.

```pyhon
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos.apps.ProductosConfig'
]
```
vamos a productly/urls.py y añadimos productos/

añadimos el include y luego crearemos un archivo productos/urls.py, pero aqui no hay que poner la extension
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]
```
**OJO**: dentro del include se ponen separado por punto no por /
En ese archivo productos/urls.py los path('',...) simbolizan /productos/. si añadimos path('lala',....) estariamos añadiendo la url /productos/lala/

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```
dara un error porque no hemos creado el metodo index, lo creamos en productos/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hola mundo')
```

probamos la aplicacion
```bash
python3 manage.py runserver
```
si navegas a http://127.0.0.1:8000/productos/ saldra el mensaje de **hola mundo**

# modelos
 
vamos a productos/models.py
dentro de models.fields. podriamos ver los tipos de datos disponibles

```python
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255) #cadena de texto limitada
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: eliminar el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina la categoria si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna el valor por defecto 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

# migraciones

una vez actualizado el modelo, toca actualizar la bbdd mediante migraciones

```bash
python3 manage.py makemigrations
```
Y nos crea el archivo productos/migrations/0001_initial.py
Si la aplicacion no estuviese registrada en INSTALLED_APPS del archivo productly/settings.py, las migraciones para la app no funcionarian

Para aplicar las migraciones hacemos
```bash
python3 manage.py migrate
```

# actualizando modelos

vamos a nuestro models.py lo editamos y damos makemigrations y migrate

# panel de administracion

```bash
python3 manage.py runserver
```
vamos a /admin

para crear un usuario y contraseña vamos a la terminal 

```bash
python3 manage.py createsuperuser
```
ponemos fer y una contraseña tonta de 123456
volvemos a arrancar el servidor

Ahora vamos a configurar los modelos para que salgan en la pantalla de administracion.
Editamos productos/admin.py

```python
from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
```

Luego añadimos una categoria. Vemos que pone Categoria.object(1) Vemos que lo pone un poco raro, ahora vamos personalizar como representa las cosas en el administrador.
Vamos a models y en la parte de categoria añadiemos el metodo string
```python
class Categoria(models.Model):
    nombre = models.CharField(max_length=255) #cadena de texto limitada
    
    def __str__(self):
        """devuelve la clase como string"""
        return str(self.nombre)
```
con esto ya pone Deportes en el nombre

Para personalizar las columnas a mostrar en el administrador de modelos, vamos a admin.py y añadimos una clase CategoriaAdmin para luego añadirla al admin.site.register
```python
from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto)
```

haremos lo mismo con el producto
```python

class Productodmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, Productodmin)
```
queremos ahora ocultar el campo creado_en a la hora de crear el producto y que se asigne con la fecha actual automaticamente
- con fields= indicamos los campos que queremos que aparezcan
- con exclude= los campos que queremos ocultar

```python
#productos/admin.py
from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class Productodmin(admin.ModelAdmin):
    exclude = ('creado_en', ) #la coma es para que se sepa que es una tupla y no un simple string
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, Productodmin)
```

# como consultar datos de bbdd

vamos a productos/views.py y hacemos un prototipo rapido
```python
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
```

# eliminar error pylintrc

en esta linea da un error aunque no impiede la ejecucion
```python
productos = Producto.objects.all().values() # todos
```
para quitarlo instalamos
```bash
pipenv install pylint-django
```
en la carpeta productly (a la altura de manage.py) creamos un archivo .pylintrc
y añadimos load-plugins=pylint-django

cuando volvemos a abrir el archivo views.py ya no vemos el error.

# plantillas

dentro de views.py comentamos los anteriores metodos y ponemos el siguiente
```python

def index(request):
    productos = Producto.objects.all()
    
    return render(
        request,
        'index.html',
        context={'productos' : productos}
    )
```
dentro de la carpeta productos creamos una carpeta llamada templates. Ahí agregamos el archivo index.html
```html
<!--templates/index.html-->
<h1>Productos</h1>
```
damos a runserver y vamos a http://127.0.0.1:8000/productos/ donde vemos que nos sale la pagina

**EMET** permite escribir las plantillas.
Al escribir esto y pulsar enter nos generara una tabla con cuatro celdas en una fila

table.table>thead>tr>th*4

nos genera esto
```html
<table class="table">
    <thead>
        <tr>
            <th></th>
            <th></th>
            <th></th>
            <th></th>
        </tr>
    </thead>
</table>
```
para añadir luego del thead el tbody ponemos tbody>tr>td*4 y damos enter.
para escribir instrucciones de python pondremos {%%} y para las variables {{ nombre_variable }}. Por cierto, el campo categoria va a funcionar porque tiene el metodo definido __str__

```html
<!--templates/index.html-->
<h1>Productos</h1>

<table class="table">
    <thead>
        <tr>
            <th>NOMBRE</th>
            <th>STOCK</th>
            <th>PUNTAJE</th>
            <th>CATEGORIA</th>
        </tr>
    </thead>
    <tbody>
        {% for producto in productos %}
        <tr>
            <td>{{ producto.nombre }}</td>
            <td>{{ producto.stock }}</td>
            <td>{{ producto.puntaje }}</td>
            <td>{{ producto.categoria }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

# agregar frameworks css

agregamos templates/base.html. escribimos ! y pusamos enter para que genere codigo html. Agregamos un bloque para el codigo
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Productly</title>
</head>
<body>
    {% block content %}

    {% endblock %}
</body>
</html>
```
esto anterior funcionara como pagina maestra o layout en otros lenguajes.

regresamos a index.html y al inicio del archivo ponemos el extends y lo encapsulamos en el bloque de contenido
```html
{% extends 'base.html' %}

{% block content %}
<!--templates/index.html-->
<h1>Productos</h1>

<table class="table">
    <thead>
        <tr>
            <th>NOMBRE</th>
            <th>STOCK</th>
            <th>PUNTAJE</th>
            <th>CATEGORIA</th>
        </tr>
    </thead>
    <tbody>
        {% for producto in productos %}
        <tr>
            <td>{{ producto.nombre }}</td>
            <td>{{ producto.stock }}</td>
            <td>{{ producto.puntaje }}</td>
            <td>{{ producto.categoria }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
```
ahora vamos a bootstrap y añadimos en base.html tanto el css como el script (el script debajo de la zona de content)

# ver video de carga de plantillas desde otras carpetas
![cargaplantillas](cargaplantillas.mp4)
hemos modificado
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        
```
y añadimos [os.path.join(BASE_DIR, 'templates')],
ahora a la altura del manage.py creamos una carpeta templates.
arrastramos el archivo base.html a esa nueva carpeta

**ATAJO** CON CTRL+P puedes navegar por los archivos por nombre como en visual studio normal

# parametros por la url

vamos al archivo productos/urls.py y añadimos una linea
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:producto_id>', view=views.detalle, name='producto_detalle')
]
```
lanzará un error cuando producto_id no sea un entero.

editamos views.py para agregar el metodo detalle
```python
def detalle(request, producto_id):
    return HttpResponse(producto_id)
```

ahora cambiamos el metodo de detalle para añadir una plantilla
```python
def detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle.html', context={'producto': producto})
```
y añadimos la template/detalle.html

div>h6+p*4

y quedara asi
```html
{% extends 'base.html' %}

{% block content %}

<div>
    <h6>{{ producto.nombre }}</h6>
    <p>{{ producto.categoria }}</p>
    <p>{{ producto.stock }}</p>
    <p>{{ producto.puntaje }}</p>
    <p>{{ producto.creado_en }}</p>
</div>

{% endblock %}
```
# pagina 404

```python
from django.http import HttpResponse, JsonResponse, Http404
from .models import Producto
#. . . .
def detalle(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        return render(request, 'detalle.html', context={'producto': producto})
    except Producto.DoesNotExist:
        raise Http404()
```
el codigo anterior se puede sustituir por algo resumido como
```python
from django.shortcuts import render, get_object_or_404

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    return render(request, 'detalle.html', context={'producto': producto})
```

# links
una forma de hacerlo
```html
  <tbody>
        {% with fila=1 %}
        {% for producto in productos %}
        <tr>
            <td><a href="/productos/{{ fila }}">
                {{ producto.nombre }}</a></td>
            <td>{{ producto.stock }}</td>
            <td>{{ producto.puntaje }}</td>
            <td>{{ producto.categoria }}</td>
        </tr>
       
        {{ fila|add:"1" }} # esto añade uno a la variable, no se pueden editar
        {% endfor %}
        {% endwith %}
    </tbody>
```
otra forma es la siguiente. Cogiendo del archivo urls.py el **name** de donde queremos ir, en nuestro caso producto_detalle
```html
    <tbody>
        {% for producto in productos %}
        <tr>
            <td><a href="{% url 'producto_detalle' producto.id %}">
                    {{ producto.nombre }}
                </a>
            </td>
            <td>{{ producto.stock }}</td>
            <td>{{ producto.puntaje }}</td>
            <td>{{ producto.categoria }}</td>
        </tr>      
        {% endfor %}
    </tbody>
```
ahora vamos a editar el urls.py para poder hacerlo mas escalable. Antes teniamos esto 
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:producto_id>', view=views.detalle, name='producto_detalle')
]
```
para evitar tener que estar poniendo producto_... hacemos lo siguiente
```python
#urls.py
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:producto_id>', view=views.detalle, name='detalle')
]
```
vemos como hemos cambiado producto_detalle por detalle unicamente y al añadir app_name (variable reservada en django) lo coge y lo aplica.
Ahora modificamos el html de antes para cambiar el producto_detalle
```html
<tbody>
        {% for producto in productos %}
        <tr>
            <td><a href="{% url 'productos:detalle' producto.id %}">
                    {{ producto.nombre }}
                </a>
            </td>
            <td>{{ producto.stock }}</td>
            <td>{{ producto.puntaje }}</td>
            <td>{{ producto.categoria }}</td>
        </tr>      
        {% endfor %}
    </tbody>
```
hemos cambiado el producto_detalle por productos:detalle

**NOTA: PARA EL RESALTADO DE SINTAXIS HTML USAR PAQUETE VSCODE LLAMADO DJANGO DE baptiste Darthenay**

# formularios

creamos un archivo forms.py dentro de productly/productos/forms.py
```python
#forms.py
from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = [
            'nombre',
            'stock',
            'puntaje',
            'categoria'
        ]
```
ahora instalamos un plugin que no viene por defecto. Vamos a productly/settings.py
añadimos django.forms
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'productos.apps.ProductosConfig',
]
```

# visualizar formularios

vamos a productly/productos/urls.py y agregamos
```python
path('formulario', views.formulario, name='formulario'),
```
vamos al views y creamos el metodo formulario
```python
#views.py
from .forms import ProductoForm
def formulario(request):
    form = ProductoForm()
    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
```
creamos la plantilla en productos/templates/producto_form.html
```html
{% extends 'base.html' %}

{% block content %}

<form 
    action="{% url 'productos:formulario' %}" 
    method='post'>

    {% csrf_token %}

    {{ form }}
    <input type="submit" value="Enviar" />
</form>

{% endblock %}
```
yendo a la siguiente url nos saldra el formulario 
http://127.0.0.1:8000/productos/formulario

vemos que ha generado un formulario con validaciones html5 y todo.