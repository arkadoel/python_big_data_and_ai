nombre_curso = "curso de python"
descripcion_curso = """
curso de python en donde
pongo varias lineas

y se imprimen
"""
print(nombre_curso, descripcion_curso)

# funcion len
print(len(nombre_curso))

# acceder a un caracter de la cadena
print(nombre_curso[0])
# sacar la palabra de 'curso'
print(nombre_curso[0:5])
# sacar desde el caracter 3 hasta el final
print(nombre_curso[3:])
# sacar hasta el caracter 9 hasta
print(nombre_curso[:9])
# asumir lo que imprimir, lo que hace es
# coger todo
print(nombre_curso[:])

# otras pruebas
print("Tamaño descripcion ", len(descripcion_curso))
print("--------------")
# 50 primeros caracteres
print(descripcion_curso[:50])
print("--------------")
