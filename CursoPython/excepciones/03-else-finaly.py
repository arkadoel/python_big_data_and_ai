try:
    n1 = int(input("Ingresa un numero: "))
    print(f"Numero {n1}")
except Exception as ex:
    print("ocurrio un error" )
else:
    print("else se ejecuta cuando no ocurrio ningun error")
finally:
    print("finally se ejecuta siempre aunque haya ocurrido error")