from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('<int:producto_id>', view=views.detalle, name='producto_detalle')
]
