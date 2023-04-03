'''veremos and or, not'''

gas = True
encendido = True

if gas and encendido:
    print("puedes avanzar")

encendido = False

if gas or encendido:
    print("puede que tengas gas o que estes encendido")

if gas or not encendido:
    print("has negado encendido")
