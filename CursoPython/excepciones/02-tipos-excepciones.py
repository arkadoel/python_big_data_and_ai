try:
    n1 = int(input("Ingresa un numero: "))
    print(f"Numero {n1}")
    variable
except ValueError as ex:
    print("ocurrio un value error" )
except NameError as ex:
    print("ocurrio un nameError" )
except Exception as ex:
    print("ocurrio un error" )