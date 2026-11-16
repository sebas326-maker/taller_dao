# validaciones y reglas del negocio
from modelo import Producto


class ProductoServicio:
    def __init__(self, dao):
        self.dao = dao

    def _validar(self, nombre, precio, stock):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

    def registrar(self, nombre, precio, stock):
        self._validar(nombre, precio, stock)
        producto = Producto(None, nombre.strip(), precio, stock)
        return self.dao.insertar(producto)

    def listar(self):
        return self.dao.listar()

    def buscar(self, id):
        producto = self.dao.buscar_por_id(id)
        if producto is None:
            raise ValueError(f"No existe un videojuego con ID {id}")
        return producto

    def actualizar(self, id, nombre, precio, stock):
        self.buscar(id)  # lanza error si no existe
        self._validar(nombre, precio, stock)
        self.dao.actualizar(Producto(id, nombre.strip(), precio, stock))

    def eliminar(self, id):
        self.buscar(id)  # lanza error si no existe
        self.dao.eliminar(id)

    def vender(self, id, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero")
        producto = self.buscar(id)
        if cantidad > producto.stock:
            raise ValueError(
                f"Stock insuficiente: solo hay {producto.stock} unidades disponibles"
            )
        producto.stock -= cantidad
        self.dao.actualizar(producto)
        return producto
