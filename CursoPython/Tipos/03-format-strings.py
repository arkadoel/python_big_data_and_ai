nombre = "Paco"
apellido = "Shen"

# forma poco elegante
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# forma elegante
nombre_completo = f"{nombre} {apellido} mide {1 + 0.80}m"
print(nombre_completo)
