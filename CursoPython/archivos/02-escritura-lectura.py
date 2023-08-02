from pathlib import Path
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init() #poner colores

archivo = Path("CursoPython/archivos/archivo-prueba.txt")

texto = archivo.read_text(encoding="utf-8").split("\n")
print(f"{Fore.YELLOW}{texto}{Fore.RESET}")

texto.insert(0, "hola mundo")

archivo.write_text("\n".join(texto), "utf-8")