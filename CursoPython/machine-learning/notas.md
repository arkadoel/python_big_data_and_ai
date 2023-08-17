# primeros pasos

![imagen](0001.png)

## herramientas populares

![imagen](0002.png)

- Jupyter.org
- Anaconda.com

Instalamos anaconda para linux
```bash
sudo chmod +x Anaconda3-2023.07-2-Linux-x86_64.sh
```
se instala en /home/*usuario*/anaconda3 o en mi caso /media/WD/OPT para no ocupar espacio en disco

probamos jupyter con 
```bash
jupyter notebook
```

damos a **new** y nuevo jpykernel
escribimos y ejecutamos hola mundo y vemos que nos guarda un archivo untitled.jpynb

# ejemplo de como desinstalar anaconda
```bash
conda install anaconda-clean
anaconda-clean --yes
rm -rf ~/anaconda3
xed .bashrc #=>eliminar la parte de conda
```

# carga de datos

descargaremos datos de kaggle.com buscamos "video game" y nos descargamos "video game sales with ratings" de rush kirubi. renombramos el archivo como vg.csv
Abrimos el archivo de jupyter y añadimos
```python
import pandas as p
df = p.read_csv("vg.csv")
df.values #podremos acceder a todos los valores que se encuentran dentro de este dataframe
```
nos devuelve un array
```python
array([['Wii Sports', 'Wii', 2006.0, ..., 322.0, 'Nintendo', 'E'],
       ['Super Mario Bros.', 'NES', 1985.0, ..., nan, nan, nan],
       ['Mario Kart Wii', 'Wii', 2008.0, ..., 709.0, 'Nintendo', 'E'],
       ...,
       ['Haitaka no Psychedelica', 'PSV', 2016.0, ..., nan, nan, nan],
       ['Spirits & Spells', 'GBA', 2003.0, ..., nan, nan, nan],
       ['Winning Post 8 2016', 'PSV', 2016.0, ..., nan, nan, nan]],
      dtype=object)
```

Otro metodo (shape) nos indica el numero de filas y columnas
```python
df.shape
```
el metodo describe() devuelve una matriz con algunas filas y algunas columnas.
- **count** nos dice cuantas filas tienen ese dato relleno y si lo restamos de las filas totales sabemos cuantas filas no tienen dato
- **mean** la media o los datos que mas se repiten
- **std** desviacion estandar: de la media, cuanto se está desviando
```python
df.describe()
```
# atajos utiles

si pulsamos h saldra los atajos de teclado de jupyter
presionando la tecla de esc pasamos al modo comando (no estamos editando ninguna celda)

- Flechas arriba y abajo para desplazarse o letra **j** y **k**
- **a** para agregar una celda antes de la celda actual
- **d (dos veces)** para eliminar la celda actual
- **para recortar**, vamos al modo de insercion (cuando estamos editando una celda). Editamos, damos escape y tecla x
- **v** para pegar una celda cortada, debajo de donde estoy
- **shift+tab** ver la documentacion de un metodo
- **shift+enter** ejecuta la linea actual
- seleccionamos con ctrl y luego ctrl+enter para ejecutar las seleccionadas.


# Explicacion del problema

![imagen](0003.png)

Por tanto queremos generar una prediccion dependiendo de los datos dados en el archivo **juegos-ml.csv**

Veremos el codigo en [notebook juegos-ml](juegos-ml.ipynb)

```python
import pandas as p
data_juegos = p.read_csv("juegos-ml.csv")
data_juegos
```

# preparando los datos

Entendemos preparar los datos a las acciones de quitar datos:
- nulos
- duplicados
- incorrectos
- no relevantes

luego dividimos en dos
- datos de entrada
- datos de salida

```python
import pandas as p
data_juegos = p.read_csv("juegos-ml.csv")
X = data_juegos.drop(columns=["juegos"])
y = data_juegos["juegos"]
```
donde X contendra las columnas de edad y genero.
donde y contendra la columna de juegos

# aprendiendo y decididiendo

Yendo a la web https://scikit-learn.org/stable/user_guide.html podremos ver los diferentes modelos que hay (como el linear model). En nuestro caso vamos a usar el "Decision Trees"

![imagen](0004.png)