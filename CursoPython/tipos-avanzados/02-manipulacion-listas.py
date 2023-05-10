mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])

mascotas[0] = "Bicho"
print(mascotas)

print(mascotas[0:3])
print(mascotas[:3])
print(mascotas[2:])
print(mascotas[-1])

# para acceder a los elementos pares de un listado
print(mascotas[::2])
print(mascotas[1::2])
print(mascotas[1:2:2])

numeros = list(range(21))
print(numeros)
# coger los numeros impares
print(numeros[1::2])
# numeros pares, comenzamos desde la posicion cero
print(numeros[::2])
