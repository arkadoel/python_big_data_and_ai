
class MiPerro: 
    patas = 4 #propiedad de clase
    def __init__(self, nombre):
        print(nombre)
        self.nombre = nombre #esto es una propiedad

    def habla(self):
        print("guau")

perro1 = MiPerro("cuchi")
perro2 = MiPerro("Cuqui")

print(perro1.nombre)
print(perro2.nombre)
print(perro1.patas) #valor patas de la instancia
print(MiPerro.patas) #aqui funciona como un estatico y cada instancia coge dicho valor