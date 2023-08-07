#viene incluido dentro de python
import sqlite3

with sqlite3.connect("CursoPython/sqlite/app.db") as conn:
    cursor = conn.cursor()

    usuarios = [
        (2, "HOLA MUNDO"),
        (3, "chanchito MUNDO"),
        (4, "HOLA chanchito")
    ]

    cursor.executemany(
        "INSERT INTO USUARIOS VALUES(?,?)",
        usuarios
    )
