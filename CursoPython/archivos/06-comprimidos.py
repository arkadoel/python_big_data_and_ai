from pathlib import Path
from zipfile import ZipFile

ruta = "CursoPython/archivos/comprimidos.zip"
ruta_extract = "/tmp/archivos"

with ZipFile(ruta, "w") as zip:
    for path in Path("CursoPython/archivos").rglob("*.*"):
        #print(path)
        if ".zip" not in str(path):
            print(path)
            zip.write(path)

print("\r\n#######################\r\n")
#lectura
with ZipFile(ruta, "r") as zip:
    print(zip.namelist()) #imprime todo el contenido
    info = zip.getinfo("CursoPython/archivos/productos.json")
    print(info.file_size, info.compress_size)
    zip.extractall(ruta_extract)