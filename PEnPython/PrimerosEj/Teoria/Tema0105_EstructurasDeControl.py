#===== RESUMEN GENERAL DE LA ESTRUCTURAS DE DATOS =====#
"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------
|       CARACTERÍSTICAS        |           LISTAS             |           TUPLAS             |            DICCIONARIOS          |          CONJUNTOS           |
|------------------------------|------------------------------|------------------------------|----------------------------------|------------------------------|
| Constructor                  |         [] ó list()          |         () ó tuple()         |   {"clave" : "valor"} o dict()   |          {} ó set()          |
| Ordenada                     |             SI               |             SI               |                SI                |             NO               |
| Mutable                      |             SI               |             NO               |                SI                |             SI               |
| Permite Duplicados           |             SI               |             SI               |                NO                |             NO               |
----------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#===============LISTAS (LIST)==============#
#==========================================#
"""
Una lista de datos es una estructura de datos ordenada, la cual quiere decir que los elementos están asociados a posiciones
siendo el 0 la primera, y mutable de elementos los cuale spueden ser de cualquier tipo. 
Para poder crear una lista se utilizan []
"""
listaElementos = ["Elemento1", "Elemento2", "Elemento3"]

# Acceder a un dato: 
"""Utilizando la posición del elemento se puede acceder a él indicando el índice."""
print(listaElementos[0])

# Modificar un dato: 
"""Utilizando la posición del elemento que se quiere modicar e igualando al nuevo valor que se quiere asociar."""
listaElementos[0] = "Elemento1 modificado"

# Agregar un elemento: 
"""Como se trata de una estructura mutable, en cualquier momento, se puede agregar un elemento a la ultima posicion de la lista."""
listaElementos.append("Elemento nuevo")

# Agregar un elemento en una posición determinada: 
"""Muy similar al caso anterior, pero indicando la posición donde se agrega (el resto se mueve a la derecha)"""
listaElementos.insert("Elemento adicional", 1)

# Eliminar un elemento: 
"""Indicando el valor del elemento que se quiere borrar, la lisa eliminar el primer elemento que coincida con el valor."""
listaElementos.remove("Elemento1")
del listaElementos[0] #Existe la posibilida de eliminar el elemento indicando la posición exacta que se quiere borrar

#== ACCIONES AVANZADAS DE LAS LISTAS ==#

# Iterar sobre los elementos:
"""Para ello es necesario utilizar la estructura de control <for>, obteniendo cada uno de los elementos de la colección de uno en uno."""
for item in listaElementos:
    print(item)

# Obtener la posición de un elemento:
"""Para ello se utiliza el método <index()>, retornando la posición del valor indicado. En el caso de no encontrarlo se retorna un <ValueError>"""
listaElementos.index("Elemento2")

# Filtrar elemento:
"""No se trata de un método como tal, sino una concatenación de sentencias de control, utilizando el <for> y el <if> de forma conjunta."""
p = [p for p in listaElementos if "2" in p]

# Ordenar una lista:
"""Utilizando el método <sort()>, pudiendo indicar entre los paréntesis la condición de ordenación"""
listaElementos.sort(key=len)


#==================TUPLAS==================#
#==========================================#
"""
Las tuplas son una estructura de datos muy similar a las listas con la diferencia que no son mutables (no se puede ni agregar ni eliminar elementos).
Para poder crear una tupla, se indican los elementos que forman parte de ella.
"""
trabajadoras = ("Juan", "Patricia", "Maria")
# Todos los método vistos en el apartado de listas se utilizan exactamente igual en el de tuplas (pero sin la posibbilidad de agregar o eliminar elementos)
"""
Es posible desempaquetar una tupla, o lo que es lo mismo, crear variables asignándolas de forma directa a los elementos de tu interior. 
Un ejemplo sería:
"""
datos = ("Ford", "Mustang", 2025, 500, 60000)
marca, modelo, anho, cv, precio = datos # Cada dato se asignará a una variable en su posición respectiva
"""
En las listas también existe la posibilidad, pero al ser una colección dinámica, el uso es más marginal.
"""

#===============DICCIONARIOS===============#
#==========================================#
"""
Los diccionarios permiten introducir datos relacionando una clave a un valor.
Es importante saber, que las claves deben ser únicas ya que es la forma de poder acceder a la información del diccionario.
Para la creación de un diccionario, se hará de la siguiente forma:
"""
trabajador = {
    "Nombre":"Carlos",
    "Edad":32,
    "Especialidad":"Tocas los huevos",
    "Titulación":"Amado lider",
    "Conocimientos": ["Programacion","Sistemas","BigData"]
}

# Accedo a elementos
"""Para poder acceder a un elemento de un diccionario, se utiliza la clave asociada. Tambiñen se puede utilizar el método <get> para el acceso."""
print(trabajador["Nombre"])

# Modificar elementos
"""Muy similar al acceso del elemento, con la diferencia que hay que indicar el nuevo valor de este."""
trabajador["Edad"] = trabajador ["Edad"] +1 

# Eliminar elementos
"""Para poder eleiminar un elemento del diccionario se utiliza la función <del>, indicando cual es el elemento que se quiere elimintar."""
del trabajador["Titulación"]

# Añadir elementos
"""En el caso de querer añadir un elemento que no exista en el diccionario, se indica la clave y el valor que tendrá."""
trabajador ["Especialidad"] = "Inteligencia Artificial" 

# Recorrer elementos
"""Utilizando la estructura de control <for> podemos acceder a las claves del diccionario y así acceder a los valores de forma iterativa."""
for item in trabajador: # Recorremos el for asociando a <item> la clave del diccionario
    print(f"{item}:{trabajador[item]}")
    if item =="conocimiento":
        for c in trabajador[item]:
            print(f"\t{c}")

#== ACCIONES AVANZADAS DE LOS DICCIONARIOS ==#

# Obtener todos los elementos
"""Para ello se utiliza el método <values>"""
for item in trabajador.values():
    print(item)

# Obtener todas las claves
"""Para ello se utiliza el método <keys>"""
for item in trabajador.key():
    print(item)

# Saber si un elemento está dentro del diccionario
"""Para ello se evalua mediante el operador <in>"""

#=================CONJUNTOS================#
#==========================================#
"""
Las colecciones de conjuntos o <set> son muy similares a las listas, con la diferencia que no se permiten elementos duplicados y además son no ordenadas.
Importante: En el caso de que hubiera un elemento duplicado, Python elimina automaticamente el ultimo dato que fuera duplicado. 
Para poder definir un conjunto se utilizan las llaves o la función <set>:
"""
numeros = {1,2,2} # utilizando las llaves
numerosSet = set( [2,3,4] ) #utilizando la funcion <set>

# Agregar datos
"""Se utiliza el metodo <add>"""
numeros.add(4)

# Eliminar datos
"""Se utiliza el método <distart> (si no exite el elemento a borrar no da error) o remove (si no existe el elemento al borrar, da error)"""
numeros.discard(5) # Si el elemento no existe en el conjunto => NO dará error
numeros.remove(5) # Si el elemento no existe en el conjunto => dará error

# Vaciar datos
"""Se utiliza el método <clear>"""
numeros.clear() 

# Recorrer los elementos
"""Se utiliza una estructura <for>"""
for i in numeros:
    print(i)

#== ACCIONES AVANZADAS DE LOS CONJUNTOS ==#
"""Los conjuntos pueden operar para realizar uniones entre si."""

# Unión
"""Se obtienen un <set> con los valores de dos conjutnos, eliminando auqellos datos que están duplicados."""
conjunto1 = {1,2,3,4,5}
conjunto2 = {3,4,5,6,7}
conjuntoUnion = conjunto1.union(conjunto2) # Resultado: {1,2,3,4,5,6,7} => Se han eliminado los duplicados

# Intersección
"""Se obtiene un <set> con los valores duplicados de dos conjutnos, eliminando auqellos que no lo son"""
conjuntoInter = conjunto1.intersection(conjunto2) # Resultado: {3, 4, 5} => Se conversan únicamente los duplicados

# Diferencia
"""Se obtiene un <set> con los valores que están en el conjunto A pero no en el B"""
conjuntoDif = conjunto1.difference(conjunto2) # Resultado {1, 2} => Se conservan los valores que únicamente estan en el conjunto 1 y no se repiten en el 2

# Diferencia Simetrica
"""Se obtiene un <set> con los valores que están en el conjunto A y B pero obviando los comunes."""
conjuntoDifSim = conjunto1.symmetric_difference(conjunto2) # Resultado {1, 2, 6, 7} => Se conversan únicamente los valore sno duplicados de ambos conjuntos.
