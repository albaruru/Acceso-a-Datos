#=========ESTRUCTURAS DE SELECCIÓN=========#
#==========================================#

# if - if/else - if/elif/else
"""
Cuando queramos que nuestro programa tome decisiones en tiempo de ejecución, utilizaremos la estructura <if> ya que, gracias a ella, Python podrá
ejercuatar un bloque u otro en función de si se cumple o no una condición booleana.
"""
numero = int(input("Por favor, introduce el valor numérico que quieres evaluar: "))

if numero > 0 or numero < 100:
    if numero <10:
        print("Valor entre 0 y 10")
    elif numero <100:
        print("Valor de 2 cifras menor que 100")
else: print("Valor no válido.")

# match
"""
En el caso de querer ejecutar un código directamente asociado al valor de una variable, la estructura <if> puede ressultar muy tediosa.
Para ello, es recomendable utilizar la estructura <match> la cual evalúa el valor de una variable y ejecuta de forma directa el caro correspondiente,
pudiendo seleccionar un caso por defecto utilizando el carácter.
"""
opcion = int(input("Slecciona una opción(1, 2 o 3)"))
match opcion:
    case 1:
        print("Has seleccionado la opción 1: Ver pefil.")
    case 2:
        print("Has seleccionado la opción 2: Editar perfil.")
    case 3:
        print("Has seleccionado la opción 3: Cerrar sesión.")
    case _: # Este es el método default del <swtich> en Java
        print("Opción no válida. Inténtalo de nuevo.")

#=========ESTRUCTURAS DE REPETICIÓN========#
#==========================================#
"""
Otro tipo de estructuras muy utilizadas son las de repetición. Estas no permiten realizar ejecución de blosques de código recurrente sin necesidad
de escriber n veces las mismas líneas.
Son muy útiles para recorrer colecciones de datos o para ejecutar recursivamente una función sobre una condición lógica.
"""

# for
"""
Este estructura permite ejecutar un bloque de código en un rango determinado (indicando un incremento). Para ello se utilizar el método <range()>, 
pasando como parámetros el valor inicial, final e incremento del código. En cada iteracción, la variable definida tomará un nuevo valor
"""
for i in range(1, 10, 3): # valor inicial = 1, valor final = 10, incremento = 3
    print(i) # Salida de datos: 1, 4 y 7
"""
En el caso de querer hacer un decremento, sería con un range a negativo
"""
for i in range (10, 1, -3):
    print(i)
"""
Otra de las opciones es indicar una colección de datos en vez del método range, pudiendo así asignar a la variable creada cada uno de llos elementos
de la colección.
"""
for i in [1,2,3,4,5,6,7,8,10]:
    print(i)

alumnos = ["Juan", "Maria", "Jorge", "Claudia", "Marcos", "Celia"]
for i in alumnos:
    print(i)
"""
Dentro de la estructura de control, se pueden utilizar tantas estructuras como sean necesarias, incluso anidar el mismo tipo de estructura.
"""
for i in range (1,10):
    print(f"Tabla del {i}")
    for j in range (1,10):
        print(f"{i} x {j} = {i*j}")

# while
"""
Esta estructura de control permite repetir un bloque de código dependiendo de una condición lógica.
Importante: La condición de evaluación tiene que cambiar en algún momento. De no ser así, el bucle entrará en un bucle infinito.
"""
contador = 1
while contador < 5:
    print("Valor:", contador)
    contador +=1
print("Saliendo del bucle while")

"""
Si hacemos un ejemplo más cercano al mundo informático, podemos utilizar un bloque <while> para dejar la aplicación bloqueada
hasta realizar un "login" correcto.
"""
nombre = input("Introduce el nombre del usuario: ")
password = input ("Introduce la pass del usuario: ")

while nombre != "admin" or password != "admin":
    print("Login incorrecto.")
    nombre = input("Introduce el nombre del usuario: ")
    password = input("Introduce la pass del usuario: ")
print("Login correcto, puedes continuar.")

"""
NOTA IMPORTANTE:
En Python, no existe la estructura de control <do-while>. Sin embaro, podriamos siular su uso con un <while(true)> y un break en el caso 
de no cumplir la condición correspondiente.
"""

while True:
    numero = int(input("Adivina el número que estoy pensando (1 al 10): "))
    if numero == 7:
        print ("Has acertado!")
        break
    print("Vuelve a intentarlo: ")
print("Saliendo del falso do-while de Python")

