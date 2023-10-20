import sqlite3

conexion = sqlite3.connect("agenda2.db")
cursor = conexion.cursor()

nuevos_socios = [("Melpene", "Rosa"), ("Melculo", "Ana Lisa")]

cursor.executemany("insert into socios values (null,?,?)", nuevos_socios)

conexion.commit()
conexion.close()
