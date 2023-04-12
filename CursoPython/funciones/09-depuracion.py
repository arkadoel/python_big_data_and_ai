#
def largo(texto):
    resultado = 0
    for char in texto:
        resultado = resultado + 1
        return resultado


print("inicio")
l = largo("hola mundo")
print(l)
