#la key siempre tiene que ser un string
punto = {"x": 25, "y": 50}
print(punto)

print(punto["x"])

punto["z"] = 45
print(punto)

if "lala" in punto:
    print(punto["lala"])


print(punto.get("x"))

print(punto.get("lala")) #como no existe pone None
print(punto.get("lala", 97)) #como no existe 97

del punto["x"]
del punto["y"]

print(punto)


punto["x"] = 35

for key in punto:
    print(key, punto[key])

for key, valor in punto.items():
    print(key, valor)


usuarios = [
    { 
        "id" : 1,
        "nombre" : "Felipe"
    },
    { 
        "id" : 2,
        "nombre" : "Pedro"
    }
]

for usuario in usuarios:
    print(usuario["nombre"])