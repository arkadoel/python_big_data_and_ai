#para ahorrarse los getter y los setter

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        return


p = Perro("Rufus")
print(p.nombre)
p.nombre = "Rufus II"
print(p.nombre)