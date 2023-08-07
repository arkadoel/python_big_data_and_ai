#viene incluido dentro de python
import sqlite3

with sqlite3.connect("CursoPython/sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS USUARIOS
        (
            ID      INTEGER PRIMARY KEY,
            NOMBRE  VARCHAR(50)
        );
        """
    )
#con el with te ahorrar el close y los commit