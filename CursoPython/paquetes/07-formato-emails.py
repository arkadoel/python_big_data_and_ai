#solo funciona con smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib


plantilla = """
    <b>hola mundo $usuario</b>
"""
template = Template(plantilla)
#dos opciones para crear el cuerpo
#cuerpo = template.substitute({ "usuario" : "chanchito feliz" })
cuerpo = template.substitute(usuario = "chanchito feliz")

path = Path("ruta-imagen/imagen.png")
imagen = MIMEImage(path.read_bytes())

mensaje = MIMEMultipart()
mensaje["from"] = "hola mundo"
mensaje["to"] = "email@destino.com"
mensaje["subject"] = "esta es una prueba"
cuerpo = MIMEText("cuerpo del mensaje", "html")
mensaje.attach(cuerpo)
mensaje.attach(imagen)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() #nos identifica
    smtp.starttls() #activar TLS

    smtp.login("usuario de google", "contraseña")
    smtp.send_message(mensaje)
    print("mensaje enviado")
