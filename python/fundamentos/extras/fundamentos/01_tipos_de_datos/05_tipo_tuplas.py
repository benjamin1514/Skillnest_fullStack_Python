# tuplas 
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

# Las tuplas agrupan un conjunto de elementos que pueden contener cualquier tipo de dato.

gato = ("Miau", 5, "persa", False)

#Para consultar la información de una tupla lo hacemos a través de su índice, tal como lo hacíamos con las listas.
print(gato[0]) #Imprime: Miau

'''
Recuerda que las tuplas son inmutables, 
por lo que al intentar cambiar el valor de algún índice obtendremos un TypeError:
'''
# gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment

# A pesar de esto, podemos agregar elementos a las tuplas o hacer slicing.
gato = gato + ("4.1",) # Forma para incorporar dentro de una lista(tipo: tupla)
print(gato) #Imprime: ('Miau', 5, 'persa', False, '4.1')

#  Funciones integradas

# len(secuencia): devuelve la longitud (cantidad de elementos) de una secuencia.
# max(secuencia): devuelve el valor más alto en una secuencia.
# min(secuencia): devuelve el valor más bajo en una secuencia.
# sorted(secuencia): devuelve una secuencia ordenada.
# sum(secuencia): devuelve la suma de los valores de la secuencia.

#  Tupla como valores return

def suma_multiplicacion(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma, multiplicacion)

print(suma_multiplicacion(10, 6))

'''
¿Por qué usar tuplas?
Inicialmente, las tuplas pueden parecer más complicadas para la manipulación de 
información, entonces ¿por qué utilizaría una tupla y no una lista?
Las tuplas pueden almacenar información y al ser inmutables garantizan que otros 
desarrolladores que utilicen tu código no puedan modificar los conjuntos de datos que necesites 
que permanezcan constantes.
'''
