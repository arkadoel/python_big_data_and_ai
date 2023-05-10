mascotas = [
    "wolfgang",
    "pelusa",
    "pulga",
    "felipe",
    "chanchito feliz",
    "pulga"
]

mascotas.insert(1, "melvin")
print(mascotas)

# agregar al final
mascotas.append("chanchito triste")
print(mascotas)

# eliminar elementos (solo elimina el primero)
mascotas.remove("pulga")  # no indice, el elemento
print(mascotas)

mascotas.pop()  # saca el ultimo elemento
print(mascotas)
mascotas.pop(1)  # sacamos a melvin
print(mascotas)

# otra forma de eliminar
del mascotas[0]
print(mascotas)

# para eleminar todos
mascotas.clear()
