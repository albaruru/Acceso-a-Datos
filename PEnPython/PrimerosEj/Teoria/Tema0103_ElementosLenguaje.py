#=================VARIABLES================#
#==========================================#

"""
Aunque no es necesario definir la variable a la hora de utilizarlas (ya que se asignan solas)
es necesario conocer los tipos para en caso de necesitar forzar su uso o similar.
Las variables son las siguientes:
"""
numeroEntero = int (1) # => números enteros sin decimal
numeroFloat = float (3.252325) # => números con decimales, donde la parte decimal se representa con un punto
cadenaDeTexto = str ("Texto") # => cadena de caracteres, definida entre <" ">
booleano = bool (True) # => valor de true o false muy utilizado para decisiones lógicas
listaDinamica = list ( ["Carlos", 7, True, 3.2567] ) # => lista ordenada y DINÁMICA para poder guardar diferentes datos
listaEstatica = tuple ( ("Carlos", 7, False, 3.2578974) ) # => lista ordenada y ESTÁTICA para poder guardar diferentes datos
diccionario = dict ( {"nombre" : "Carlos", "numero" : 7, "boolean" : True , "numeroDecimal" : 3.2526} ) # => diccionario de datos asociando par clave-valor

#==================MÉTODOS=================#
#==========================================#

# input () 
"""Permite leer por teclado un dato y asociarlo a una variable. Pide como parámetros el texto que se mostrará en la petición."""
nombre = input ("Método input(): Introduce tu nombre: ") # pedimos al usuario que introduzca su nombre

# print ()
"""Escribe por consola el texto indicado como parámetro."""
print ("Método print(): Mensaje a mostrar") # mostramos por consola el mensaje

# upper () o lower ()
"""Estos métodos permiten pasar a mayuscula o minúscula respectivamente un texto indicado por parámetros."""
print ("Método upper():" , nombre.upper()) # el texto se mostrará en mayusculas
print ("Método lower():" , nombre.lower()) # el texto se mostrará en minúsculas

# strip ()
"""Permite eliminar espacios en blanco de un <string> pasado por parámetros."""
nombre2 = "    Texto para utilizar strip()  "
nombreLimpio = nombre2.strip() # elimina los espacios del principio y del final de la cadena de texto. Podemos especificar lo que deseamos eliminar dentro del parentesis
print("Método strip()")
print(nombre2) # texto original y con espacios
print(nombreLimpio) # limpiamos los espacios en blanco

# replace ()
"""Permite sustituir un grupo de caracteres por otro en un <string>."""
print("Método replace()")
nombre3 = "Juan"
print("Nombre Original:" , nombre3)
nombre3 = nombre3.replace("Juan" , "Juanjo")
print("Nombre Modificado" , nombre3) #reemplazamos un nombre por otro

# find ()
"""Permite obtener la posición de un grupo de caracteres en una palabra, retornando su posición."""
print("Método find()")
nombre4 = "Juan Gómez"
posicion = nombre4.find("Gómez")
print(nombre4)
print("El apellido Gómez empieza en la posicion:",posicion) #buscamos la posición del apellido en la cadena de texto

# len()
"""Retorna la longitud del objeto que se pasa por parámetro, siendo la cantidad de letras en el caso de pasar un <string> o un número en el caso de pasar una lista"""
print("Método len()")
palabra = input("Escribe una palabra:")
print(f"La palabra {palabra} tiene {len(palabra)} caracteres.") #mostramos la longitud de la palabra

# type()
"""Retorna la clase del objeto que se pasa por parámetros."""
print("Método type(): El tipo de dato de la variable es:" , type(nombre4)) # mostramos el tipo de dato que es la variable

#================OPERADORES================#
#==========================================#

# OPERADORES BINARIOS

a = 10
b = 3
"""(-)  Resta aritmética entre dos operadores"""
resta = a - b #Resta: 7
"""(+)  Suma aritmética entre dos operadores"""
suma = a + b #Suma: 13
"""(*)  Multiplicación aritmética entre dos operadores"""
multi = a * b #Multi: 30
"""(**) Potencia aritmética de la base y el exponente"""
expon = a**b #Potencia: 10^3 = 1000
"""(/)  División aritmética entre dos operadores"""
div = a/b  #Division: 3.3333
div = a//b #Division entera: 3
"""(%)  Resto aritmético entre dos operadores. Se trata del resto de la división entre dos números"""
modulo = a % b #Módulo: 1

# OPERADORES COMPARACIÓN

"""
(>)  Operador mayor que otro
(>=) Operador es mayor o igual que otro
(<)  Operador es menor que otro
(<=) Operador es menor o igual que otro
(==) Operador es igual que otro
(!=) Operador es diferente que otro
"""

# OPERADORES LÓGICOS
"""
(and) Obtiene como resultado <true> si todas las condiciones de la sentencia son verdaderas 
(or)  Obtiene como resultado tru si una de las condiciones de la sentencia es verdadera.
(not) Obtiene el valor booleano inverso del booleano indicado.
"""