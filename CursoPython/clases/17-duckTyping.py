
'''
    eliminamos modelo y abc y como tienen el mismo metodo
    sigue funcionando. Debido al tipado dinamico
    "camina como pato y parece un pato, es un pato"
'''


class Usuario():
    def guardar(self):
        print("guardando en bbdd")

class Sesion():
    def guardar(self):
        print("guardando en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])