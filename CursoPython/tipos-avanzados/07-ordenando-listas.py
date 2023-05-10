numeros = [2, 4, 1, 45, 75, 22]
numeros.sort()
print(numeros)

# ordenar alreves
numeros.sort(reverse=True)
print(numeros)

numeros = [2, 4, 1, 45, 75, 22]
# sorted va a devolver una nueva lista,
# mientras que sort modifica la lista existente
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [
    [4, "chanchito"],
    [1, "felipe"],
    [5, "pulga"]
]
usuarios.sort()
print(usuarios)

# ahora vemos que fallara el ordenado
usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]
usuarios.sort()
print(usuarios)

# para ordenarlo correctamente hacemos lo siguiente
usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# creamos un metodo que devuelve el campo numerico


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena, reverse=True)
print(usuarios)

# lo anterior se ve fatal y es poco intuitivo, otra forma
# mirar el siguiente archivo
