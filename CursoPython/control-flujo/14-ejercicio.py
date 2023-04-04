"""
Aplicacion de calculadora
"""

primer_num_ingresado = ""

print("Bienvenido a la calculadora, para salir escribe Salir")

if primer_num_ingresado == "":
    primer_num_ingresado = input("Ingrese el primer numero: ")

while True:
    ingresar_op = input("Ingrese una operacion: ")

    if ingresar_op.lower() == "salir":
        break
    segundo_num_ingresado = input("Ingrese otro numero: ")

    resultado = ""
    ingresar_op = ingresar_op.lower()
    n1 = float(primer_num_ingresado)
    n2 = float(segundo_num_ingresado)

    if ingresar_op == "suma":
        resultado = n1 + n2
    elif ingresar_op == "resta":
        resultado = n1 - n2
    elif ingresar_op == "multi":
        resultado = n1 * n2
    elif ingresar_op == "division":
        resultado = n1 / n2
    else:
        print("El tipo de operacion no es valida.")

    if resultado != "":
        print(f"Resultado {resultado}")

        primer_num_ingresado = str(resultado)
