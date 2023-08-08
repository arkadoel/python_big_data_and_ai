# vamos a obtener las preguntas que hay en stackoverflow

# pipenv install beautifulsoup4


import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url)
print(respuesta.status_code)
texto = respuesta.text
soup = BeautifulSoup(texto, "html.parser")

preguntas = soup.select(".s-post-summary")
print(preguntas[0]["data-post-id"]) #id de la pregunta cero

for pregunta in preguntas:
    titulo = pregunta.select_one(".s-link").get_text()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"({usuario.strip()}) - {titulo.strip()}")

