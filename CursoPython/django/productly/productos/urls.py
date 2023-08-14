from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', view=views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('<int:producto_id>', view=views.detalle, name='detalle')
]
