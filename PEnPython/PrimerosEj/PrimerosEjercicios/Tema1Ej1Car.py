# UNIDAD 01 - TEMA 01 - EJERCICIO 01 DEL TEMARIO #
#================================================#
"""
Realiza el siguiente ejercicio para practicar lo visto en esta unidad:
Imagina que tienes dos jugadores que introducen su puntuaciones. El programa debe:
1.- Pedir el nombre y la puntuación de cada jugador.
2.- Mostrar operaciones aritméticas entre las puntuaciones (suma, diferencia, etc...)
3.- Comparar las puntuaciones y mostrar los resultador (==, >, <, etc...)
4.- Mostrar expresiones lógicas compuestas sobre quién tiene más puntos, si son iguales, etc.
5.- Mostrar todos los resultados como parte de un resumen
"""

#Declaracion de variables
jugador1 = input("Introduce el nombre del Jugador 01: ")
j1p1 = int(input("Puntuación de la primera ronda: "))
j1p2 = int(input("Puntuación de la segunda ronda: "))
j1p3 = int(input("Puntuación de la tercera ronda: "))
puntuacionTotal1 = j1p1 + j1p2 + j1p3
mediaPuntuacion1 = float(puntuacionTotal1 / 3)

jugador2 = input("Introduce el nombre del Jugador 02: ")
j2p1 = int(input("Puntuación de la primera ronda: "))
j2p2 = int(input("Puntuación de la segunda ronda: "))
j2p3 = int(input("Puntuación de la tercera ronda: "))
puntuacionTotal2 = j2p1 + j2p2 + j2p3
mediaPuntuacion2 = float(puntuacionTotal2 / 3)

print(" ")
print("|=====TABLA RESUMEN DEL PARTIDO:====|")
print("|-----------------------------------|")
print("|            JUGADOR 01             |")
print(f"| Ronda 01: {j1p1}")
print(f"| Ronda 02: {j1p2}")
print(f"| Ronda 03: {j1p3}")
print(f"| Total:    {puntuacionTotal1}")
print(f"| Media:    {mediaPuntuacion1}")
print("|-----------------------------------|")
print("|            JUGADOR 02             |")
print(f"| Ronda 01: {j2p1}")
print(f"| Ronda 02: {j2p2}")
print(f"| Ronda 03: {j2p3}")
print(f"| Total:    {puntuacionTotal2}")
print(f"| Media:    {mediaPuntuacion2}")
print("|-----------------------------------|")
print(" ")

if mediaPuntuacion1 > mediaPuntuacion2:
    print(f"EL GANADOR DEL ENCUENTRO ES: {jugador1.upper()}")
elif mediaPuntuacion1 == mediaPuntuacion2:
    print(f"LOS JUGADORES {jugador1.upper()} Y {jugador2.upper()} HAN QUEDADO EN EMPATE.")
else:
    print(f"EL GANADOR DEL ENCUENTRO ES: {jugador2.upper()}")