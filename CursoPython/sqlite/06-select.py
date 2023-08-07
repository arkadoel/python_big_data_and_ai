import sqlite3

with sqlite3.connect("CursoPython/sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("select * from usuarios")
    print(cursor.fetchone()) #leemos una


#select all

with sqlite3.connect("CursoPython/sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute("select * from usuarios")
    print(cursor.fetchall()) #leemos todo