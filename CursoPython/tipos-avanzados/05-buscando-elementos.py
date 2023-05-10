mascotas = ["pelusa", "pulga", "felipe", "chanchito feliz", "pulga"]

indice = mascotas.index("pulga")
print(indice)

if "wolfgang" in mascotas:
    print("existe en posicion " + mascotas.index("wolfgang"))

print("contador", mascotas.count("pulga"))
