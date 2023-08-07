import sys
from pathlib import Path
import os

print(sys.argv)

def cli(args):
    if len(args) == 1:
        print("no hay argumentos")
        return
    elif len(args) == 3:
        print("no hay 2 argumentos")
        return
    else:
        origen = args[1]
        o = Path(origen)
        if not o.exists():
            print("origen no existe")
            return
        
        destino = args[2]
        d = Path(destino)
        if not d.exists():
            print("destino no puede existir")
            return
        
        os.rename(str(origen), str(destino))
        print("archivo renombrado con exito")

if __name__ == "__main__":
    cli(sys.argv)