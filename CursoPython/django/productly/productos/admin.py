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
