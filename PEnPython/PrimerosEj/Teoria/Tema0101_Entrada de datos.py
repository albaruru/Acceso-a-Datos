#=========ENTRADA Y SALIDA DE DATOS========#
#==========================================#

#Método para imprimir por consola 
print("")
print("Método de salida por consola con print") 

#Los f-string evitan la utilización de la concatenación con el comando "+"
print("")
nombre = "Carlos"
print(f"Formateando la salida de consola con f-string por parte de {nombre}")

#Los f-string permiten actuar sobre el contenido de la variable, como en el siguiente código que permite ver la cantidad de letras con "len" delante de la variable
print("")
nombre = "Carlos"
correo = "carlos@gmail.com"
print(f"El correo de {nombre} es {correo}, el cual cuenta con {len(correo)} caracteres.") # La función len() permite obtener la longitud de los caracteres del string

#Para la entrada de datos, utilizamos el método "input"
print("")
nombre = input("Cual es tu nombre? ") 
correo = input("Cual es tu correo? ") #Utilizamos el input para recoger por consola los datos y dentro del parentesis introducimos el mensaje
edad = input("Cual es tu edad? ")
print(f"Hola soy {nombre}, mi correo es {correo} y mi edad es {edad}")

#Al utilizar input, los datos introducidos por consola son string pero podemos realizar una conversion de la siguiente forma
print("")
edad = int(input("Cual es tu edad? ")) #La variable será un int desde que se recoge
