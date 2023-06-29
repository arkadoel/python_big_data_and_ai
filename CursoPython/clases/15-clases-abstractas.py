'''
    debemos cambiar model para que no se pueda hacer una
    nueva instancia de esa clase
'''
from abc import ABC, abstractmethod



class Model(ABC):
    # quitamos tabla = False

    #eliminamos el constructor
    
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(123)