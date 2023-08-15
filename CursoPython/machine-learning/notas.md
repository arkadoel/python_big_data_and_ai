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
