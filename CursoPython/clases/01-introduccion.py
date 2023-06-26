mensaje = "hola mundo"

print(type(mensaje))

class MiPerro: #PascalCase
    def habla(self):
        print("guau")


mi_perro = MiPerro() # no hace falta new como en c#
print(type(mi_perro))
mi_perro.habla()

print(isinstance(mi_perro, MiPerro))