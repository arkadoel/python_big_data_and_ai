#metodos que se ejecutan automaticamente como el constructor
# los metodos magicos se usan poniendo punto __
#basicamente el override de c#

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice guau!")
    
    def __str__(self):
        return f"{self.nombre} dice guau!"
    
    # metodo destructor
    def __del__(self):
        print("chao perro")

p = Perro("Rufus", 7)
print(str(p))
del p # llamara al destructor para eliminar la instancia de perro
