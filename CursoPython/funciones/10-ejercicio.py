"""
los palindromos son frases o palabras que se pueden leer en cualquier direccion
"""


def replace_espacios(texto):
    salida = ""

    for i in range(0, len(texto)):
        if texto[i] != " ":
            salida += texto[i]
    return salida


def reverse_text(texto):
    texto_reverso = ""
    final_texto = len(texto)-1
    final_iteracion = -1  # para que llegue a imprimir la posicion cero
    salto_contador = -1

    for i in range(final_texto, final_iteracion, salto_contador):
        texto_reverso += texto[i]

    return texto_reverso


def es_palindromo(texto):
    resultado = False
    # texto = texto.replace(' ', '')  # quitar espacios
    texto = replace_espacios(texto)
    texto = texto.lower()  # pasamos a minusculas
    texto_inicial = texto
    texto_final = reverse_text(texto)

    return texto_inicial == texto_final


print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola mundo", es_palindromo("hola mundo"))

"""
Resultados esperados:
true
true
true
false
"""
