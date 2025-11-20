"""
OBJETIVO:
Crear un programa que:
1.Pida los nombres de varios alumnos.
2.Permita introducir varias notas para cada alumno.
3.Calcule la media de cada alumno.
4.Indique si está APROBADO (media ≥ 5) o SUSPENSO (media < 5).
5.Muestre un resumen final con todos los alumnos y la cantidad total procesada.

REQUISITOS:
1.Usar listas y diccionarios para guardar los datos.
2.Utilizar bucles (while y for) y condicionales (if/else).
3.Validar que las notas sean números válidos.
4.Permitir finalizar la entrada de alumnos o notas dejando el campo vacío (Enter).
"""

# Mostrar título
print("=== GESTOR DE NOTAS ===")

# Lista principal para guardar alumnos
alumnos = []

# Bucle principal para introducir alumnos
while True:
    nombre = input("Introduce el nombre del alumno (o pulsa Enter para finalizar): ")
    if nombre == "":
        break  # Salir si no se escribe nada

    # Lista de notas del alumno actual
    notas = []
    while True:
        nota = input("Introduce una nota (o pulsa Enter para terminar): ")
        if nota == "":
            break  # Salir si no se escribe nada
        try:
            notas.append(float(nota))  # Convertir a número decimal
        except ValueError:
            print("Por favor, introduce un número válido.")

    # Guardar alumno en un diccionario
    alumno = {"nombre": nombre, "notas": notas}
    alumnos.append(alumno)

# Mostrar resultados finales
print("\n=== RESULTADOS ===")
for alumno in alumnos:
    if len(alumno["notas"]) > 0:
        media = sum(alumno["notas"]) / len(alumno["notas"])
    else:
        media = 0

    estado = "APROBADO" if media >= 5 else "SUSPENSO"
    print(f"{alumno['nombre']}: media = {media:.2f} -> {estado}") #.2f es redondeamos a 2decimales FLOAT

# Mensaje final
print("\n--- Fin del programa ---")
print(f"Se han procesado {len(alumnos)} alumnos.")