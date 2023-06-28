''' propiedades y metodos privados
    vamos a cambiar la propiedad nombre a privada
'''


class MiPerro: 
    
    def __init__(self, nombre, edad):
        print(nombre)
        self.__nombre = nombre #ahora es privada
        self.edad = edad

    def habla2(self): 
        print(f"guau1 {self.__nombre}")

    @classmethod
    def factory(cls):
        return cls("perrito numero", 4)
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    #para hacer metodos privados, simplemente añadir dos guiones bajos
    # def __metodo_privado(self, nombre):
    #     pass

p = MiPerro.factory()
p.habla2()
# print(p.__nombre) #dara error por no ser accesible
print(p.get_nombre())

#para acceder a todas las propiedades de una instancia
print(p.__dict__) #es mala practica editar este diccionario