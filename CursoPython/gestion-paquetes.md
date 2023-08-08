
# pypi

https://pypi.org/

por ejemplo buscando django nos sale:

```bash
pip install Django
```

# pip

```bash
pip3 --version
pip3 install requests
pip3 list =>lista los paquetes instalados
sudo pip3 uninstall requests
pip3 install requests==2.18.1
pip3 install requests==2.*

python3 -m pip install --upgrade pip
python3 -m pip install paquete => forzar
```

# 03 ambientes virtuales

```bash
python3 -m venv env
#para activar el ambiente hacemos lo siguiente
source env/bin/activate
#lo podremos ver en la carpeta lib, por ejemplo instalamos requests
pip3 install requests
#para desactivar el ambiente virtual
deactivate
```
Genera una carpeta env con diferentes subcarpetas. las librerias se instalan dentro de lib y dentro de la carpeta bin podremos tener el ejecutable de python.

# pipenv

```bash
pip3 install pipenv
pipenv install requests
```
genera dos archivos **Pipfile** y **Pipfile.lock**
para ver donde se agrego la carpeta env ponemos
```bash 
pipenv --venv 
```
en mi caso /home/nuc/.local/share/virtualenvs/paquetes-_BlTIyqt

para activar el ambiente virtual de pipenv hacemos
```bash 
pipenv shell
```

para salir del ambiente virtual usamos exit
```bash 
exit
```
_______________________________
para que nos coja las configuraciones de pipfile borramos la carpeta del ambiente y volvemos poner pipenv install

```bash
rm -rf /home/nuc/.local/share/virtualenvs/paquetes-_BlTIyqt
pipenv install #en la carpeta donde tenemos el pipfile
```

si queremos que use pipfile.lock y no pipfile usamos
```bash
pipenv install --ignore-pipfile #en la carpeta donde tenemos el pipfile.lock
```

# gestionar dependencias instaladas

Mostrar dependencias instaladas

```bash
pipenv graph
```
desinstalamos requests
```bash
pipenv uninstall requests
```
instalar version especifica
```bash
pipenv install requests==2.10.*
```
Para actualizar los paquetes a su ultima version
```bash
pipenv update --outdated
#como nos pone un skipped editamos el pipfile y ponemos la version 2.* en vez de la 2.10.* y ya nos saldra como actualizable

#actualizamos
pipenv update #=> para todos
pipenv update requests # solo un paquete
#y nos actualizó a la version 2.31.0
```

# crear paquete y documentando un paquete

Creamos la carpeta holamundoplayer donde creamos una carpeta llamada igual holamundoplayer

Documentando archivo player.py

```python
"""
Fer, esta es la documentacion de player
"""

class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song:str):
        """
        Reproduce la cancion que recivio
        
        Parameters:
        song (str): este es un string con el path de la cancion

        Returns:
        int: devuelve 1 si reproduce correctamente, sino devuelve cero
        """
```