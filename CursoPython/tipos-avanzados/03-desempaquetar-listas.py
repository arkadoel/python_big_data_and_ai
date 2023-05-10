numeros = [1, 2, 3]

# vamos a hacer el siguiente codigo de otra manera
primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

# asi se puede hacer de otra forma
primero, segundo, tercero = numeros
print(primero, segundo, tercero)


# obtener el primer elemento de listado solamente
primero, *otros = numeros
print(primero)
print(otros)

# ahora solamente queremos los dos primero elementos
primero, segundo, *otros = numeros

# ahora el primer elemento y el ultimo
primero, *otros, ultimo = numeros

# segundo y penultimo
primero, segundo, *otros, penultimo, ultimo = numeros
