import csv
import os

ruta = "./CursoPython/archivos/archivo.csv"
with open(ruta, "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["tweet_id", "user_id", "text"])
    writer.writerow([1000, 1, "esto es un tweet"])
    writer.writerow([1001, 2, "esto es otro tweet"])

#leer
with open(ruta, "r") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in list(reader):
        print(linea)

#modificar
ruta_temp = "./CursoPython/archivos/archivo_temp.csv"
with open(ruta, "r") as rfile, open(ruta_temp, "w") as wfile:
    reader = csv.reader(rfile)
    writer = csv.writer(wfile)
    rfile.seek(0)
    for linea in list(reader):
        if linea[0] == "1000":
            writer.writerow([1000, 1, "esto modifica tweet"])
        else:
            writer.writerow(linea)
        
    os.remove(ruta)
    os.rename(ruta_temp, ruta)