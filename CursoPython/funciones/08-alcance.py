#
el_saludo = ""


def saludar():
    saludo = "hola mundo"
    el_saludo = saludo


def saludaChanchito():
    saludo = "hola chanchito"
    el_saludo = saludo


# print(saludo)
""" 
el 'alcance' se refiere al ambito o contexto de las variables
en este caso fallaria porque la variable 'saludo' solo esta definida con un 
ambito dentro de los metodos.
"""

#####################
saludar()
saludaChanchito()
saludar()
"""llamar a varios metodos no altera las variables que estos contienen porque
estas no son globales"""

# ahora añadimos una variable global
el_saludo = ""
saludar()
print(f"el saludo: {el_saludo}")
saludaChanchito()
print(f"el saludo: {el_saludo}")
saludar()
print(f"el saludo: {el_saludo}")
"""pese a que 'el saludo' es una variable global,no se ve afectada cada vez que 
es modificada en los metodos"""

# PYTHON NO ADMITE VARIABLES GLOBALES
"""en caso de querer usar una variable global deberiamos de poner los siguiente
en el metodo. usar palabra 'global'"""


def metodo():
    global el_saludo
    saludo = "otro texto"
    el_saludo = saludo


metodo()
print(f"el saludo tras metodo: {el_saludo}")
