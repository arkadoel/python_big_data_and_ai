#las tuplas pueden ser creadas pero no se pueden modificar
numeros = (1, 2,3) +(4,5,6)
print (numeros)

#crear tuplas en base a un listado
punto = tuple([1, 2])
print(punto)

menos_numeros = numeros[:2]
print(menos_numeros)

#desempaquetar las tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)

#para modificar una tupla debemos volcarlo en otra variable como una
#lista y modificarlo

lista_numeros = list(numeros)
lista_numeros[0] = "texto"
print(lista_numeros)
numeros = tuple(lista_numeros)
print(numeros)