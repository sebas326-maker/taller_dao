# Sistema de Inventario de Videojuegos

**Estudiante:** Sebastian Andres Mercado Vega
**Curso:** Acceso a Datos 4E

## Propósito del sistema

Aplicación de consola en Python para administrar el inventario de una tienda de videojuegos. Permite registrar, consultar, actualizar y eliminar videojuegos (CRUD) y registrar ventas que descuentan unidades del stock. La información se guarda en una base de datos **SQLite**, por lo que se conserva entre ejecuciones. Se aplica el **patrón DAO** para separar el acceso a datos de la lógica del programa.

## Estructura del proyecto

```
├── evidencias/            # capturas de pantalla de las pruebas
├── README.md
├── base_datos.py          # conexión y creación de la base de datos
├── main.py                # menú interactivo en consola
├── modelo.py              # clase Producto
├── producto_dao.py        # operaciones SQL (CRUD)
└── producto_servicio.py   # validaciones y reglas del negocio
```

| Archivo | Responsabilidad |
|---|---|
| `modelo.py` | Clase `Producto` con id, nombre, precio y stock. |
| `base_datos.py` | Crea la conexión a `inventario.db` y la tabla `productos` si no existe. |
| `producto_dao.py` | Clase `ProductoDAO`: contiene todas las consultas SQL (insertar, listar, buscar, actualizar, eliminar). |
| `producto_servicio.py` | Clase `ProductoServicio`: valida los datos y aplica las reglas del negocio antes de usar el DAO. |
| `main.py` | Menú interactivo. No contiene SQL; solo usa los métodos del servicio. |

## Funciones implementadas

1. **Registrar videojuego:** pide nombre, precio y cantidad disponible.
2. **Mostrar inventario:** lista todos los videojuegos con ID, nombre, precio y stock.
3. **Buscar videojuego:** consulta un producto por ID e informa si no existe.
4. **Actualizar videojuego:** modifica nombre, precio y stock de un producto existente.
5. **Eliminar videojuego:** elimina un producto por su ID.
6. **Vender unidades:** pide el ID y la cantidad, y descuenta las unidades del inventario.
0. **Salir:** finaliza la aplicación.

### Validaciones

- No se permiten nombres vacíos.
- No se aceptan precios menores o iguales a cero.
- No se permiten cantidades de inventario negativas.
- No se permiten ventas con cantidades menores o iguales a cero.
- No se puede vender más unidades de las disponibles.
- Se informa cuando el ID solicitado no existe.
- Las entradas incorrectas (por ejemplo, letras en lugar de números) no cierran el programa.

## Cómo ejecutarlo

Requisitos: Python 3.8 o superior. SQLite viene incluido con Python, no hay que instalar nada más.

```bash
git clone <URL-DEL-REPOSITORIO>
cd <carpeta-del-repositorio>
python main.py
```

La primera vez se crea automáticamente el archivo `inventario.db`.

## Evidencias de pruebas

| Prueba | Resultado esperado | Resultado obtenido | Evidencia |
|---|---|---|---|
| Registrar Resident Evil 4 con precio 180000 y stock 10 | Producto guardado correctamente | Correcto | `evidencias/registro.png` |
| Mostrar inventario | Aparecen los productos registrados | Correcto | `evidencias/Inventario.png` |
| Buscar un ID existente | Se muestran los datos del producto | Correcto | `evidencias/Buscar.png` |
| Actualizar un producto | Los cambios quedan guardados en SQLite | Correcto | `evidencias/Actualizar.png` |
| Vender 3 unidades de Resident Evil 4 | El stock pasa de 10 a 7 | Correcto | `evidencias/vender.png` |
| Intentar vender 20 unidades | Se rechaza la operación y se conserva el stock | Correcto | `evidencias/vender_20.png` |
| Buscar un ID inexistente | Se informa que no existe | Correcto | `evidencias/Busqueda_inexistente.png` |
| Eliminar un producto | El producto deja de aparecer en el inventario | Correcto | `evidencias/Eliminar.png` |

### Operación exitosa: venta de 3 unidades

![Venta exitosa](evidencias/venta_exitosa.png)

### Operación rechazada: venta de 20 unidades

![Venta rechazada](evidencias/venta_rechazada.png)
