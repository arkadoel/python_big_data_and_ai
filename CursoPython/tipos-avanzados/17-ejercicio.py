from pprint import pprint
# eliminar los espacios en blanco de un string
texto = "texto para el primer ejercicio"

def quita_espacios(texto):
    return [char for char in texto if char != " "]

sin_espacios = quita_espacios(texto)
print(texto)

# contar en un diccionario cuantas veces se repite 
# los caracteres de un string

def cuenta_caracteres(lista):
    letras_dict = {}
    for letra in lista:
        if letra in letras_dict:
            letras_dict[letra] +=1
        else:
            letras_dict[letra] = 1
    
    return letras_dict

contador = cuenta_caracteres(sin_espacios)
pprint(contador, width=1)

# ordenar las llaves de un diccionario por el valor que tienen
# y devolver una lista que contiene tuplas [("a",3), ("b", 2), . . . ]

def ordena(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda key: key[1],
        reverse=True
    )

ordenados = ordena(contador)
print(ordenados)

# de un listado de tuplas, devolver las tuplas que tengan
# el mayor valor

def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

mayores = mayores_tuplas(ordenados)
print(mayores)

# crear un mensaje que diga:
# los caracteres que mas se repiten son C y D

def crea_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones\n"
    return mensaje

print(crea_mensaje(mayores))
