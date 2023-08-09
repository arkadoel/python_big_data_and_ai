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

Ahora vamos a configurar los modelos para que salgan en la pantalla de administracion