import json
from pathlib import Path

productos = [
    {"id": 1, "name": "suftboard"},
    {"id": 2, "name": "bicicleta"},
    {"id": 3, "name": "skate"}
]

data = json.dumps(productos)
print(data)
ruta = "CursoPython/archivos/productos.json"
Path(ruta).write_text(data, encoding="utf-8")

#leer json
data = Path(ruta).read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

#modificar json
productos[0]["name"] = "chanchito feliz"
finaljson = json.dumps(productos)
Path(ruta).write_text(finaljson, encoding="utf-8")

#leer json
data = Path(ruta).read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)