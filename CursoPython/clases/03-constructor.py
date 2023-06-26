
class MiPerro: 

    def __init__(self, nombre):
        print(nombre)
        self.nombre = nombre

    def habla(self):
        print("guau")

perro1 = MiPerro("cuchi")
perro2 = MiPerro("Cuqui")

print(perro1.nombre)
print(perro2.nombre)