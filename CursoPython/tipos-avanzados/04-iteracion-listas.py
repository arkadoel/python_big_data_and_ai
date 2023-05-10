mascotas = ["pelusa", "pulga", "felipe", "chanchito feliz"]

for mascota in mascotas:
    print(mascota)

# ahora queremos un indice en donde se encuentran
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
