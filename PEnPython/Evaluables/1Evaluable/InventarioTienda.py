#   Descripción:
#   Sistema básico de gestión de inventario para una tienda de productos electrónicos.
#
#   Funcionalidades:
#    1. Cargar inventario desde inventario.txt
#    2. Mostrar inventario
#    3. Calcular valor total del inventario
#    4. Identificar productos agotados
#    5. Actualizar cantidad de un producto

import os # Modulo para ver si el archivo exisate

# nombre del archivo donde guardamos el inventario
ARCHIVO = "inventario.txt"


# 1. GUARDAR INVENTARIO EN INVENTARIO.TXT
# Guarda los productos y los datos en el acchivo, con la W sobreescribe el archivo
with open(ARCHIVO, "w", enconding="utf-8") as f:
    for nombre, datos in inventario.items():
        precio, cantidad = datos
        f.write(f"{nombre}), {precio}, {cantidad}\n")

        #el archivo se cierra automaticamente al usar WITH



# 2. CARGAR INVENTARIO DESDE EL ARCHIVO INVENTARIO.TXT
def cargar_inventario():
    inventario = {}
    #comprobamos si el archivo existe
    if not os.path.exists(ARCHIVO):
        #Inventario inicial predeterminado
        inventario_inicial ={
            "Portatil": [799.99,10],
            "Teléfono": [299.99, 5],
            "Tablet": [199.99, 0],
        }
        guardar_inventario(inventario_inicial)
        return inventario_inicial
    
    #Si el archivo existe, leemos sus lineas
    with open(ARCHIVO, "r", encoding="uft-8") as f:
        for linea in f:
            linea = linea.strip() #quitamos espacios y saltos de linea
            nombre, precio, cantidad = linea.split (",")
            inventario[nombre] = [float(precio),int(cantidad)]
    return inventario


# 3. MOSTRAR INVENTARIO
def mostrar_inventario(inventario):
    #Imprime todos los productos del inventario de forma legible.
    print ("/n--- INVENTARIO DE PRODUCTOS ---")
    for nombre, datos in inventario.items():
        precio, cantidad = datos
        print(f"Producto: {nombre} | Precio: {precio}€ | Cnatidad: {cantidad}")


# 4. CALCULAR VALOR TOTAL INVENTARIO
def valor_total(inventario):
    total = 0
    for precio, cantidad in inventario.values():
        total+= precio * cantidad
    return total


# 5. IDENTIFICAR PRODUCTOS AGOTADOS
def productos_agotados(inventario):
    return [nombre for nombre, datos in inventario.items() if datos[1] ==0]


#6. ACTUALIZAR CANTIDAD DE PRODUCTO
def actualizar_cantidad(inventario):
    mostrar_inventario(inventario)

    producto=input("Ingresa el nombre del producto que quieres actualizar: ")

    if producto not in inventario: 
        print ("El producto no existe.\n")
        return inventario
    try:
        nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
    except ValueError:
        print ("Debes ingresar un numero entero.\n")
        return inventario
    
    #Actualizamos y guardamos
    inventario[producto][1] = new_cantidad
    guardar_inventario(inventario)

    print("Cantidad actualizada. \n")
    return inventario


# 7. MENU PRINCIPAL
inventario = cargar_inventario()

while True:
    print("== MENÚ DE INVENTARIO ==")
    print("1. Mostrar inventario")
    print("2. Calcular valor total")
    print("3. Ver productos agotados")
    print("4. Actualizar cantidad de un producto")
    print("5. Salir") 

    opcion = input ("Selecciona una opcion: ")

    if opcion == "1":
        mostrar_inventario(inventario)
    
    elif opcion == "2":
        print(f"Valor total del inventario: {valor_total(inventario)}€\n")
        
    elif opcion == "3":
        agotados = productos_agotados(inventario)
        if agotados:
            print("Productos sin stock" , ", ".join(agotados), "\n")
        else:
            print("No hay productos agotados. \n")

    elif opcion == "4":
        inventario = actualizar_cantidad(inventario)
    
    elif opcion == "5":
        print ("Saliendo del programa...")
        break
    
    else:
        print("Opcion invalida. Intenta nuevamente.\n")


# 8. METODO MAIN PYTHON
# Esta línea hace que el programa se ejecute solo si este archivo
# se ejecuta directamente y no si se importa en otro archivo.
if __name__ == "__main__":
    menu()