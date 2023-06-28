
class MiPerro: 
    patas = 4 
    def __init__(self, nombre, edad):
        print(nombre)
        self.nombre = nombre 
        self.edad = edad

    def habla(self): #metodo de la instancia
        print("guau")

    @classmethod
    def habla2(cls): #metodo de clase y cls es para referirse a la clase misma
        print("guau1")

    @classmethod
    def factory(cls):
        return cls("perrito numero", 4)
    
print(MiPerro.habla2())

#podremos hacer lo siguiente haciendo un "factory method"
perro1 = MiPerro("cuchi",2)
perro2 = MiPerro("Cuqui", 3)
#haciendo lo siguiente
perro3 = MiPerro.factory()
print(perro3.edad, perro3.nombre)

