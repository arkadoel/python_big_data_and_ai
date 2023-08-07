import random

print(random.random()) #entre 0 y 1

print(random.randint(1,10)) #entre 1 y 10

lista = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista) #no se puede poner directamente ne el print porque modifica la lista directamente
print(lista)

lista2 = [1,2,3,4,5,6,7,8,9]
print(random.choice(lista2)) #coge valor aleatorio de la lista


print(random.choices(lista2, k=3) )