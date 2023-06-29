class Model():
    tabla = False

    def __init__(self) -> None:
        if not self.tabla:
            print("tienes que definir la tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(123)