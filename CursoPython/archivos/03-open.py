from io import open

#escritura
texto = "hola mundo"
ruta = "./CursoPython/archivos/hola.txt"
archivo = open(ruta, "w")
archivo.write(texto)
archivo.close()

# solamente lectura
archivo = open(ruta, "r")
texto = archivo.read()
archivo.close()
print("texto leido: " + texto)

# lectura como lista
archivo = open(ruta, "r")
texto = archivo.readlines()
archivo.close()
print("texto leido como lineas: ", texto)

#cierra los archivos automaticamente
with open(ruta, "r") as archivo:
    #archivo.__enter__ #se ejecuta cuando abramos el archivo
    #archivo.__exit__ #se ejecuta cuando se cierra el archivo
    print(archivo.readlines())
    archivo.seek(0) #volver a leer desde el inicio del archivo
    for linea in archivo: #carga de una en una las lineas del archivo en memoria
        print(linea)


#agregar
archivo = open(ruta, "a+")
archivo.write("otra linea")
archivo.close()

#lectura y escritura
with open(ruta, "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "chanchito feliz"
    archivo.writelines(texto)

archivo = open(ruta, "r")
texto = archivo.read()
archivo.close()
print("texto leido: " + texto)