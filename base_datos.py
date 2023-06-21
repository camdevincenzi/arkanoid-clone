import sqlite3
from puntuacion import Puntuacion

def crear_base_de_datos(text):
    with sqlite3.connect("db_ranking.db") as conexion:

        try:
            sentencia = ''' create table puntajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla de puntajes")
        except sqlite3.OperationalError:
            print("La tabla puntajes ya existe")

        try:
            conexion.execute("insert into puntajes(nombre,puntaje) values (?,?)", (text, Puntuacion.puntuacion))
            conexion.commit()
        except:
            print("Error")

        cursor = conexion.execute("SELECT * FROM puntajes")
        for fila in cursor:
            print(fila)