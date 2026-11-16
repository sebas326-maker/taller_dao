# mostrar el menu y recibir datos
import os
from base_datos import inicializar_bd
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

dao = ProductoDAO()
servicio = ProductoServicio(dao)


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresiona Enter para continuar...")


def pedir_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número entero")


def pedir_decimal(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número válido")


def registrar():
    nombre = input("Nombre: ")
    precio = pedir_decimal("Precio: ")
    stock = pedir_entero("Stock: ")
    id_nuevo = servicio.registrar(nombre, precio, stock)
    print(f"\nVideojuego guardado correctamente (ID {id_nuevo})")


def mostrar():
    productos = servicio.listar()
    if not productos:
        print("El inventario está vacío")
        return
    print("=== INVENTARIO ===")
    for p in productos:
        print(p)


def buscar():
    id = pedir_entero("ID a buscar: ")
    print()
    print(servicio.buscar(id))


def actualizar():
    id = pedir_entero("ID a actualizar: ")
    actual = servicio.buscar(id)
    print(f"\nDatos actuales: {actual}\n")
    nombre = input("Nuevo nombre: ")
    precio = pedir_decimal("Nuevo precio: ")
    stock = pedir_entero("Nuevo stock: ")
    servicio.actualizar(id, nombre, precio, stock)
    print("\nVideojuego actualizado correctamente")


def eliminar():
    id = pedir_entero("ID a eliminar: ")
    servicio.eliminar(id)
    print("\nVideojuego eliminado correctamente")


def vender():
    id = pedir_entero("ID del videojuego: ")
    cantidad = pedir_entero("Cantidad a vender: ")
    p = servicio.vender(id, cantidad)
    print(f"\nVenta realizada. Stock restante de {p.nombre}: {p.stock}")


def menu():
    print("=== SISTEMA DE INVENTARIO DE VIDEOJUEGOS ===")
    print("1. Registrar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar videojuego")
    print("5. Eliminar videojuego")
    print("6. Vender unidades")
    print("0. Salir")


def main():
    inicializar_bd()
    acciones = {
        "1": registrar,
        "2": mostrar,
        "3": buscar,
        "4": actualizar,
        "5": eliminar,
        "6": vender,
    }
    while True:
        limpiar()
        menu()
        opcion = input("\nElige una opción: ").strip()
        if opcion == "0":
            print("\nHasta luego")
            break
        if opcion not in acciones:
            print("\nOpción no válida")
        else:
            try:
                limpiar()
                acciones[opcion]()
            except ValueError as error:
                print(f"\nError: {error}")
            except Exception as error:
                print(f"\nOcurrió un error inesperado: {error}")
        pausar()


if __name__ == "__main__":
    main()
