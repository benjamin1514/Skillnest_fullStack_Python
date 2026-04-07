# Bucles 

# Bucles for con range

# Range con 1 argumento

for i in range(4):
    print(i)
    
#  Range con 2 argumentos

for i in range(2, 8):
    print(i)
    


#  Range con 3 argumentos 

for i in range(2, 10, 3): # 2 inicio, 10 Final del range y 3 Cuantos números se salta 
    print(i)
    
    
for i in range(0, 15, 3):
    print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):
    print(i)
#Imprime: 10, 7, 4


# Recorrer cadenas con bucles for 
'''
Los bucles pueden ser utilizados para recorrer cualquier secuencia en Python.
Gracias a esto podemos iterar cada valor de una cadena a través de un for.
'''

for letra in 'Python':
    print(letra)
#Imprime: 'P', 'y', 't', 'h', 'o', 'n'

# Recorrer listas con bucles for

lista = ['brócoli', 'pepino', 'pimiento']

for i in range(len(lista) ):
    print(i, lista[i])
#Imprime: 0 brócoli, 1 pepino, 2 pimiento
# Te da el indice de cada lugar de la lista al reccorerlo en el bucle

for verdura in lista:
    print(verdura)
#Imprime: brócoli, pepino, pimiento

# Recorrer tuplas con bucles for

'''
Las iteraciones funcionan de la misma manera para las tuplas que lo recorridos que hacemos en una lista.
'''

tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
    print(i, tupla[i])
#Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
    print(fruta)
#Imprime: fresa, manzana, cereza


# Recorrer diccionarios con bucles for
'''
Los diccionarios también pueden ser recorridos. Al hacer la iteración a través de un diccionario, 
el iterador es cada una de las claves establecidas en el diccionario.
'''
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
    print(clave)
#Imprime: nombre, curso

'''
Ya tenemos las claves, ahora ¿cómo accedemos al valor? ¡Colocando la clave entre corchetes! Veamos:
'''
estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
    print(estudiante[clave])
#Imprime: Gonzalo, Python


'''
En el capítulo de diccionarios vimos algunos métodos que nos permitían obtener 
las secuencias con los valores, claves y elementos de un diccionario. 
Prueba el siguiente fragmento de código para ver su funcionamiento en acción:
'''

platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves
for clave in platillos_tipicos.keys():
    print(clave)
#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores
for valor in platillos_tipicos.values():
    print(valor)
#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
    print(clave, "=", valor)
#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado



# Control de Bucles

# Break

'''
La sentencia break termina de forma definitiva el bucle y 
continúa con la primera sentencia después del bucle. 
El break se puede utilizar tanto para bucles for como para while.
'''

'''
El break suele utilizarse cuando sucede 
alguna condición externa que demanda salir del bucle de manera inmediata.
'''

# Por ejemplo: 

for letra in "detente":
    if letra == "n":
        break
    print(letra)
#Imprime: d, e, t, e

