from pathlib import Path

path = Path("/media/WD/PROYECTOS/2023/python_big_data_and_ai/python_big_data_and_ai/CursoPython/rutas")
# path.exists()
# path.mkdir()
# path.rmdir() #solo si esta vacio
# path.rename("chanchito-feliz")
for p in path.iterdir():
    print(p)
print("--------------------------------")
archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

print("--------------------------------")
archivos = [p for p in path.glob("*.py")]
print(archivos)

print("--------------------------------")
archivos = [p for p in path.glob("01-*.py")]
print(archivos)

print("--------------------------------")
#todos los archivos que se encuentren contenidos en la carpeta superior
archivos = [p for p in path.glob("**/**/*.py")]
print(archivos)

print("--------------------------------")
#todos los archivos que se encuentren contenidos en la carpeta superior
archivos = [p for p in path.rglob("*.py")] #recursivo
print(archivos)