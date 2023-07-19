
#sin inyeccion de dependencias
import usuario

def guardar():
    usuario.guardar()

#con inyeccion
def guardar(entidad):
    entidad.guardar()
