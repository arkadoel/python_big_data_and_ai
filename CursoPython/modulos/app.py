#from usuario import * #importariamos todo, es una mala practica
from usuarios.acciones import guardar, pagar_impuestos

guardar()
pagar_impuestos()

#los nombres de modulos usan snake_case como nombre de archivo

'''los modulos apuntan a archivos 
y los paquetes apuntan a carpetas'''

'''
 from usuarios import acciones #como es un paquete podemos importar esto
 para usarlo pondriamos
 acciones.guardar()
'''

#para hacer sub paquetes
from usuarios.otras_acciones.utilidades import prueba_sub_paquete
prueba_sub_paquete()

import usuarios

print(dir(usuarios)) #lista los paquetes dentro de un import

print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)

print(usuarios.gestion.__name__)
print(usuarios.gestion.__package__)
print(usuarios.gestion.__path__)
print(usuarios.otras_acciones.__file__)

