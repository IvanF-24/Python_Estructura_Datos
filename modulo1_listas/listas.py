# 1. Definir inventario con tres productos [nombre, cantidad, precio]
inventario = [
    ["manzana", 50, 1.2],
    ["banana", 30, 0.8],
    ["naranja", 40, 1.0]
]

# 2. Actualizar precio
def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"Precio de {producto} actualizado a {nuevo_precio}")
            return
    print("Producto no encontrado")

# 3. Registrar venta
def registrar_venta(producto, cantidad):
    for item in inventario:
        if item[0] == producto:
            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada: {cantidad} de {producto}")
            else:
                print("Stock insuficiente")
            return
    print("Producto no encontrado")

# 4. Añadir producto o actualizar stock
def anadir_producto(producto, cantidad, precio):
    for item in inventario:
        if item[0] == producto:
            item[1] += cantidad
            print(f"Stock actualizado de {producto}")
            return
    inventario.append([producto, cantidad, precio])
    print(f"Producto {producto} añadido")

# 5. Mostrar inventario
def mostrar_inventario():
    print("\nInventario actual:")
    for item in inventario:
        print(f"Producto: {item[0]}, Cantidad: {item[1]}, Precio: {item[2]}")

# --- PRUEBAS ---

# Actualizar precio del segundo producto
actualizar_precio("banana", 0.9)

# Registrar venta del primer producto
registrar_venta("manzana", 10)

# Añadir producto nuevo
anadir_producto("pera", 25, 1.5)

# Mostrar inventario final
mostrar_inventario()