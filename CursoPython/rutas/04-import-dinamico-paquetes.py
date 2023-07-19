from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]
'''importariamos db, api,... y
en dependencias sustituimos donde pone "esto es la api" por la clase
que controla la api'''

dependencias = {
    "db" : "base de datos",
    "api" : "esta es la api",
    "graphql" : "esto es graphql"
}

def load(p):
    print(str(p).replace("/", "."))
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene metodo init")


list(map(load, paths))