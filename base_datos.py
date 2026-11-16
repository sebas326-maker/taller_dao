# conexion y creacion de la base de datos SQLite
import sqlite3

NOMBRE_BD = "inventario.db"


def obtener_conexion():
    return sqlite3.connect(NOMBRE_BD)


def inicializar_bd():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()
