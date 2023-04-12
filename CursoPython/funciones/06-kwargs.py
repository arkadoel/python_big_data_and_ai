# keyword arguments

def get_product(**datos):
    print(datos)
    print(datos["id"])
    # print(datos["name"]) falla en el primer metodo que no tiene dicho parametro


get_product(id="id1")
# obligatoriamente hay que asignar un nombre de parametro
# **datos sera por tanto un diccionario

get_product(id="id2",
            name="nombre",
            numero=32)
