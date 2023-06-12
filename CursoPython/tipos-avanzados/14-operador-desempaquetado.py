lista = [1,2,3,4]
#queremos imprimir algo como 
#print(1,2,3,4)
print(*lista)

#def n(n1,n2,n3) => lo podriamos hacer con n(*n)

#para combinar listas
lista2 = [5,6]
combinada = [*lista, *lista2]
print(combinada)

combinada2 = ["hola",*lista,"mundo", *lista2]

#con diccionarios con dos **
punto1 = {"x" : 13}
punto2 = {"y" : 16}
nuevopunto = {**punto1, **punto2}
print(nuevopunto)