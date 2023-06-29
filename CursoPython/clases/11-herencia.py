class Animal:
    def comer(self):
        print("comer")

#la clase de perro va a heredar de animal
class Perro(Animal) :
    def pasear(self):
        print("paseando")
    
class Chanchito(Perro): #esto se llama herencia multi nivel y en python funciona mal
    def programar(self):
        print("programar")

perro = Perro()
perro.comer()
perro.pasear()
chanchito = Chanchito()
chanchito.comer()
chanchito.pasear()
chanchito.programar()