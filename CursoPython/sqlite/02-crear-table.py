#viene incluido dentro de python
import sqlite3

con = sqlite3.connect("CursoPython/sqlite/app.db") #si no existe , la crea

cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS USUARIOS
    (
        ID      INTEGER PRIMARY KEY,
        NOMBRE  VARCHAR(50)
    );
    """
)
con.commit() #obligatorio para escribir en la bbdd
con.close()