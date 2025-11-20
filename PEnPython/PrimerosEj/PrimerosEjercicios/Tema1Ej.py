"""
Ejercicio 1: Operaciones aritméticas y sentencias de control básicas

Enunciado del ejercicio:
Se desea realizar un programa que trabaje con tres números enteros introducidos por el usuario.
El programa debe:
    1. Solicitar al usuario tres números enteros (num1, num2, num3).
    2. Mostrar los números introducidos, indicando su tipo de dato (int).
    3. Calcular y mostrar:
        o El mayor y el menor.
        o La suma de los tres números.
        o La resta secuencial (num1 - num2 - num3).
        o El producto (num1 * num2 * num3).
        o El cociente real de dividir la suma entre 3 (/).
        o La división entera (//) de la suma entre 3.
        o El resto (%) de la suma entre 3.
        o La potencia del mayor elevado al menor.
    4. Convertir la media aritmética a entero (con int) y mostrarla.
    5. Convertir la suma a cadena de texto y mostrar el mensaje: "La suma como texto es: <valor>".
    6. Indicar si la suma es par o impar.
    7. Mostrar si la media real es mayor, menor o igual a 10.

Restricciones:
    • No usar bucles ni listas.
    • Solo trabajar con variables simples y if, elif, else.
"""

# 1. Solicitar al usuario tres números enteros
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
num3 = int(input("Introduce el tercer número entero: "))

# 2. Mostrar los números y su tipo
print(f"\nNúmeros introducidos:")
print(f"num1 = {num1}, tipo: {type(num1)}")
print(f"num2 = {num2}, tipo: {type(num2)}")
print(f"num3 = {num3}, tipo: {type(num3)}")

# 3. Calcular mayor y menor
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Calcular suma, resta secuencial y producto
suma = num1 + num2 + num3
resta = num1 - num2 - num3
producto = num1 * num2 * num3

# Cociente real, división entera y resto
cociente_real = suma / 3 #una media se suman los datos que tengamos y lo dividimos entre el n de datos
division_entera = suma // 3 #es lo mismo que una media pero solo tenemos en cuenta n enteros
resto = suma % 3 #resto

# Potencia del mayor elevado al menor
potencia = mayor ** menor

# Mostrar resultados
print("\n--- Resultados Matemáticos ---")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Suma: {suma}")
print(f"Resta secuencial: {resta}")
print(f"Producto: {producto}")
print(f"Cociente real de la suma entre 3: {cociente_real}")
print(f"División entera de la suma entre 3: {division_entera}")
print(f"Resto de la suma entre 3: {resto}")
print(f"Potencia del mayor elevado al menor: {potencia}")

# 4. Media aritmética convertida a entero
media_entera = int(cociente_real)
print(f"Media aritmética como entero: {media_entera}")

# 5. Suma como cadena de texto
suma_texto = str(suma) #se convierte en string y listo
print(f"La suma como texto es: {suma_texto}")

# 6. Indicar si la suma es par o impar
if suma % 2 == 0: #si se /2 y es 0 es par
    print("La suma es par")
else:
    print("La suma es impar")

# 7. Comparar media real con 10
if cociente_real > 10:
    print("La media real es mayor que 10")
elif cociente_real < 10:
    print("La media real es menor que 10")
else:
    print("La media real es igual a 10")