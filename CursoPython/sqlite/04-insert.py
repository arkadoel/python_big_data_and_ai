#viene incluido dentro de python
import sqlite3

with sqlite3.connect("CursoPython/sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO USUARIOS VALUES(?,?)",
        (1, "HOLA MUNDO")
    )
