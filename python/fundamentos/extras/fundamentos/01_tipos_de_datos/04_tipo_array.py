# Arrays (listas)
lista_vacia = []
lista_compras = ['tomate', 'pan', 'queso', 'jamón']


# A diferencia de otros lenguajes, las listas en Python pueden tener distintos tipos de datos, cadenas, números, inclusive otras listas o tuplas.
lista_especial = [1, 2, ['a', 'b', 'c'], True]

verso1 = ['dale', 'a', 'tu', 'cuerpo']
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)


cajonera = ["pantalones", "camisetas", "calcetines"]
print(cajonera[0]) #Accedemos al cajón con índice 0. Imprime: "pantalones"
print(cajonera[1]) #Accedemos al cajón con índice 1. Imprime: "camisetas"
print(cajonera[2]) #Accedemos al cajón con índice 2. Imprime: "calcetines"
cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']


# Manipular listas

cajonera.append("vestidos") #Agregamos "vestidos" al final de la lista
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines', 'vestidos']

# Slicing 
'''
Algo de gran utilidad en Python es algo llamado Slicing o “Troceado”, 
que nos permite regresar una copia de parte de nuestra lista en base a índices específicos. 
La síntaxis utilizada es: [x:y], 
donde x es el índice inicial y y el índice final.
'''
lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]
print(lista_grande[3:]) #Imprime:[8, 10, 12, 14, 16]
print(lista_grande[:6]) #Imprime:[2, 4, 6, 8, 10, 12]
print(lista_grande[3:6]) #Imprime:[8, 10, 12]

# Funciones integradas

# len(secuencia): Regresa la cantidad de elementos en la secuencia.

vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales)) #Imprime: 5

# Métodos específicos de Listas

frozen = ["Elsa", "Anna", "Olaf"]
frozen.pop() #Sintaxis: nombre_lista.funcion()
print(frozen) #Imprime: ['Elsa', 'Anna']

# Algunos métodos comunes para las listas son
# list.append(valor): añade un valor al final de la lista.
# list.pop(índice): elimina un valor en la posición dada. Si no se pasa ningún parámetro, se eliminará el último valor en la lista.
# list.index(valor): devuelve el índice (posición) del valor dado si existe en la lista y genera un error si no existe.
# list.reverse(): invierte el orden de los elementos, en su lugar.*
# list.sort(): ordena los elementos de menor a mayor, o alfabéticamente para cadenas.


