# operaciones SQL (CRUD) sobre la tabla productos
from base_datos import obtener_conexion
from modelo import Producto


class ProductoDAO:

    def insertar(self, producto):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)",
                (producto.nombre, producto.precio, producto.stock),
            )
            conexion.commit()
            return cursor.lastrowid
        finally:
            conexion.close()

    def listar(self):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, precio, stock FROM productos ORDER BY id")
            return [Producto(*fila) for fila in cursor.fetchall()]
        finally:
            conexion.close()

    def buscar_por_id(self, id):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (id,)
            )
            fila = cursor.fetchone()
            return Producto(*fila) if fila else None
        finally:
            conexion.close()

    def actualizar(self, producto):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE productos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
                (producto.nombre, producto.precio, producto.stock, producto.id),
            )
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            conexion.close()

    def eliminar(self, id):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
            conexion.commit()
            return cursor.rowcount > 0
        finally:
            conexion.close()
