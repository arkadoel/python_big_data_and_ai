def hola(nombre, apellidos="Feliz"):
    print(f"Hola, tu nombre es {nombre} {apellidos}")
    # nombre es un parametro de la funcion


if __name__ == "__main__":
    # lo que pasamos son los argumentos de la funcion
    hola("Fernando", "Saenz")
    hola("Pedro")  # argumento opcional
