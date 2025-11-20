#===============COMENTARIOS================#
#==========================================#

#Este es un comentario de una sola linea en Python
"""
Este es un comentario
de varias lineas de código
en Python
"""

#=================VARIABLES================#
#==========================================#

"""
Las variables no necetan del tipado, ya que este se asigna con el valor en el momento de la asignación.
Ejemplo:
"""
nombre = "Carlos" # => Esta variable se recoge como una <string> directamente
num = 1 # => Esta variable se recoge como un <int> directamente

#==================BLOQUES=================#
#==========================================#

"""
Los bloques no tienen llaves como en Java <{}>.
Los bloques (tipo funciones, sentencias de control o similares) se realiza a través de sangrías.
Otra de las cosas importantes en el lenguaje es que no es necesario el uso del <;> para indicar el final de una lina, 
Ejemplo
"""
edad = int(input("Cual es tu edad?"))
if edad < 18:
    print("El usuario es menor de edad, por lo que no puede acceder a la plataforma.")
else:
    print(f"El usuario es mayor de edad.")
