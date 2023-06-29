class Animal:
    def comer(self):
        print("comer")


class Perro:
    def pasear(self):
        print("paseando")
    
class Chanchito(Perro,Animal):
    def programar(self):
        print("programar")

chanchito = Chanchito()
chanchito.comer()
chanchito.pasear()
chanchito.programar()

'''el problema de la herencia multiple es que si hay un metodo
igual en dos clases coge las clases desde la izquierda
por tanto para (Perro, Animal) si tienen el mismo metodo, se 
ejecutara el definido en Perro por estar a la izquierda
'''