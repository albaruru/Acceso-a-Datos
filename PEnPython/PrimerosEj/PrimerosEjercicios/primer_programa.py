print("hola alba")
nombre = "alba"


"formato salida"
print(f"hola alba") 
correo = "alba@gmail.com"
print(f"El correo de {nombre} es {correo}, el cual cuenta con {len(correo)} caracteres")


nombre = input("¿Cuál es tu nombre? ")
correo = input("¿Cuál es tu correo? ")
edad = input("¿Cuál es tu edad? ")

edad = int(input("¿Cuál es tu edad? "))

# petición de datos al usuario
nombre = input("¿Cuál es tu nombre? ")
correo = input("¿Cuál es tu correo? ")
edad = int(input("¿Cuál es tu edad? "))
""""
salida de datos por consola
método de salida por consola con print y mostrar los datos obtenidos
"""
print(
f"El correo de {nombre} es {correo}, el cual cuenta con {len(correo)} caracteres con {edad} años" )


if edad < 18: print("El usuario es menor de edad, por lo que no puede acceder a la plataforma")
else: print( f"El correo de {nombre} es {correo}, el cual cuenta con {len(correo)} caracteres con {edad} años")


