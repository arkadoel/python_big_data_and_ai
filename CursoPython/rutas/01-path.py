from pathlib import Path

Path(r"c:\user\windows") #la r es para no tener que poner \\
Path("/usr/bin")
print(Path())
print(Path.home())
print(Path("one/_init_.py")) #ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()
print(path.name,
      path.stem,
      path.suffix,
      path.parent,
      path.absolute()
      )

p = path.with_name("chanchito.py")
print(p)
p = path.with_suffix(".bat")
print(p)
#p = path.with_stem("loro")
#print(p)