# clase que representa un videojuego del inventario
class Producto:
    def __init__(self, id, nombre, precio, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | Precio: ${self.precio:,.0f} | Stock: {self.stock}"
