# 1. Pedir el nombre y la puntuación de cada jugador.
# 2. Mostrar operaciones aritméticas entre las puntuaciones (suma, diferencia, etc.).
# 3. Comparar las puntuaciones y mostrar los resultados (==, >, <, etc.).
# 4. Mostrar expresiones lógicas compuestas sobre quién tiene más puntos, si son iguales, etc.
# 5. Mostrar todos los resultados como parte de un resumen divertido

#1. Pedimos el nombre del usuario
jugador1 = input("Introduce tu nombre jugador 1: ")
jugador2 = input("Introduce tu nombre jugador 2: ")
# Pedimos las puntuaciones y las convertimos a números
punt1 = float(input("Introduce tu primera puntuacion: "))
punt2 = float(input("Introduce tu segunda puntuacion: "))

print(f"Hola {jugador1}!")
print(f"Hola {jugador2}!")

#2. Hacemos las operaciones
suma= punt1 + punt2
resta= punt1 - punt2
multiplicacion= punt1 * punt2
division= punt1 / punt2
division_entera = punt1 // punt2
modulo = punt1 % punt2
potencia = punt1 ** punt2

#Mostramos por pantalla
print(f"Vamos con las operaciones aritmeticas con las puntuaciones:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")

#Hacemos las operaciones y las mostramos por pantalla
print(f"{punt1} + {punt2} = {punt1 + punt2}")
print(f"{punt1} - {punt2} = {punt1 - punt2}")
print(f"{punt1} * {punt2} = {punt1 * punt2}")
print(f"{punt1} / {punt2} = {punt1 / punt2}")
print(f"{punt1} // {punt2} = {punt1 // punt2}")
print(f"{punt1} % {punt2} = {punt1 % punt2}")
print(f"{punt1} ** {punt2} = {punt1 ** punt2}")

#3. Hacemos las comparaciones
igual = punt1 == punt2
diferente = punt1 != punt2 # ¿a es distinto de b? → True
mayor_que = punt1 > punt2 # ¿a es mayor que b? → True
menor_que = punt1 < punt2 # ¿a es menor que b? → False
mayor_o_igual = punt1 >= punt2 # ¿a es mayor o igual que b? → True
menor_o_igual = punt1 <= punt2 # ¿a es menor o igual que b? → False

# Mostramos resultados de comparaciones
print("\nComparaciones:")
print(f"{punt1} == {punt2} → {igual}")
print(f"{punt1} != {punt2} → {diferente}")
print(f"{punt1} > {punt2} → {mayor_que}")
print(f"{punt1} < {punt2} → {menor_que}")
print(f"{punt1} >= {punt2} → {mayor_o_igual}")
print(f"{punt1} <= {punt2} → {menor_o_igual}")

#Hacemos las comparaciones y las mostramos por pantalla, sin haberlas hecho anteriormente.
print("\nComparaciones: ")
print(f"{punt1} == {punt2} → {punt1 == punt2}")
print(f"{punt1} != {punt2} → {punt1 != punt2}")
print(f"{punt1} > {punt2} → {punt1 > punt2}")
print(f"{punt1} < {punt2} → {punt1 < punt2}")
print(f"{punt1} >= {punt2} → {punt1 >= punt2}")
print(f"{punt1} <= {punt2} → {punt1 <= punt2}")

# 4. Expresiones lógicas compuestas
print("\nExpresiones Lógicas: ")
print(f"¿Ambos jugadores tienen la misma puntuación? {igual}")
print(f"¿Al menos uno tiene más de 50 puntos? {(punt1 > 50) or (punt2 > 50)}")
print(f"¿Ambos tienen más de 50 puntos? {(punt1 > 50) and (punt2 > 50)}")
print(f"¿El Jugador1 tiene más puntos que Jugador2 o son iguales? {mayor_o_igual}")

# 5. Resumen divertido
print("\nResumen:")
if punt1 > punt2:
    print(f"¡{jugador1} gana esta ronda con {punt1} puntos!")
elif punt2 > punt1:
    print(f"¡{jugador2} gana esta ronda con {punt2} puntos!")
else:
    print(f"¡Empate! Ambos jugadores tienen {punt1} puntos, ¡qué igualdad!")