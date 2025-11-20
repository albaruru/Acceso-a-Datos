"""
OBJETIVO: 
1.Crear un programa que permita registrar productos en una tienda y calcular el valor total del inventario.
REQUISITOS
1.Mostrar un mensaje de bienvenida al iniciar el programa.
2.Permitir introducir varios productos, cada uno con:
    Nombre del producto (texto)
    Cantidad en stock (entero)
    Precio por unidad (decimal)
3.La entrada de productos debe continuar hasta que el usuario deje el nombre vacío.
4.Validar que la cantidad y el precio sean números válidos (controlar errores con try/except).
5.Guardar los productos en una lista de diccionarios, por ejemplo:
6.Al finalizar, recorrer la lista y mostrar cada producto en el formato:
7.Calcular y mostrar el valor total del inventario.
8.Mostrar un mensaje de fin de programa.
"""

# Mostrar título
print("=== GESTOR DE INVENTARIO ===")

# Lista para guardar los productos
productos = []

# Bucle principal para introducir productos
while True:
    nombre = input("Introduce el nombre del producto (o pulsa Enter para terminar): ")
    if nombre == "":
        break  # Salir si no se escribe nada

    # Pedir cantidad en stock
    while True:
        cantidad = input("Cantidad en stock: ")
        try:
            cantidad = int(cantidad)
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # Pedir precio por unidad
    while True:
        precio = input("Precio por unidad (€): ")
        try:
            precio = float(precio)
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Guardar producto como diccionario
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    productos.append(producto)

# Mostrar listado de inventario
print("\n=== LISTADO DE INVENTARIO ===")
valor_total_inventario = 0
for producto in productos:
    valor_producto = producto["cantidad"] * producto["precio"]
    valor_total_inventario += valor_producto
    print(f"{producto['nombre']}: {producto['cantidad']} unidades x {producto['precio']} € = {valor_producto:.2f} €")

# Mostrar valor total del inventario
print(f"Valor total del inventario: {valor_total_inventario:.2f} €")
print("--- Fin del programa ---")
