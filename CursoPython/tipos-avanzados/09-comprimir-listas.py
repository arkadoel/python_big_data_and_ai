usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

# solamente queremos un listado de nombres

# haremos lo equivalente a este codigo
# nombre = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

#transformar (map)
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# filtrar (filter)
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# filtrar y transformar
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
