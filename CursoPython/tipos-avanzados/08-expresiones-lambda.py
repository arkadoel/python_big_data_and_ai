usuarios = [
    ["chanchito", 4],
    ["felipe", 1],
    ["pulga", 5]
]

#usuarios.sort(key=lambda parametros:valorRetorno)
usuarios.sort(key=lambda elem: elem[1])
print(usuarios)
