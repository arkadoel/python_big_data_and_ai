# variables de entorno

creamos un archivo .env y ponemos

```python
SENDGRID_API_KEY = "alsdkjalksdjlasdjflkajdsf"
```

instalamos el espacio virtual
```bash
pipenv install sendgrid
```
vamos a ejecutar, si nos da NONE, deberemos de poner en la shell
```bash
pipenv shell 
```
el cual va a sacar un mensaje de
```bash
Loading .env environment variables...
Loading .env environment variables...
```

y ya podemos ejecutar python3 01-env.py 
**luego añadimos el .env en el .gitignore, para que no suba**