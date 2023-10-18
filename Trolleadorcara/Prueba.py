import sqlite3

conexion = sqlite3.connect("agenda2.db")
cursor = conexion.cursor()

socios = [("suarez", "ricardo"), ("perez", "luis")]

cursor.executemany("insert into socios values (null,?,?)", socios)

conexion.commit()
conexion.close()
