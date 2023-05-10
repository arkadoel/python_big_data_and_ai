usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

#transformar (map)
#nombres = [usuario[0] for usuario in usuarios]
# filtrar (filter)
#nombres = [usuario for usuario in usuarios if usuario[1] > 2]

nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
