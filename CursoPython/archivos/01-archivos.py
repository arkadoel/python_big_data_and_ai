from pathlib import Path
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init() #poner colores

archivo = Path("CursoPython/archivos/archivo-prueba.txt")

# archivo.exists()
# archivo.rename()
# archivo.unlink() #eliminar el archivo
print(f"{Fore.GREEN}{Style.BRIGHT}actual path {Fore.RESET} {Style.RESET_ALL}{os.getcwd()}")
if (archivo.exists()):
    print(f"{Fore.YELLOW}", archivo.stat(), Fore.RESET)
else:
    print("ruta no encontrada")

from time import ctime #para ver fechas unix
acceso = archivo.stat().st_atime #en formato unix
creacion = archivo.stat().st_ctime #en formato unix
modificacion = archivo.stat().st_mtime #en formato unix

print(f"fecha de acceso {ctime(acceso)}")
print(f"fecha de creacion {ctime(creacion)}")
print(f"fecha de modificacion {ctime(modificacion)}")