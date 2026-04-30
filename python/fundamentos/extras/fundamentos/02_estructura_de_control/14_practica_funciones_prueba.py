'''
Requisitos obligatorios
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)

'''



'''
Ejercicio 1 
Crear una función que reciba una 
lista de números enteros y muestre cuál es el número mayor y cuál es el menor.
'''
def listado(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número mayor es {mayor}\nEl número menor es {menor}")

def mayorMenor():
    limit = int(input("Ingrese un límite de valores: "))
    i = 1
    listadoNum = []
    while i <= limit:
        num = int(input(f"Ingrese un número entero {i} de {limit}: "))
        listadoNum.append(num)
        i += 1
    listado(listadoNum)

'''
Ejercicio 2
Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene.
'''

def vocales(palabra):
    vocales = "aeiouáéíóú"
    contarVocales = 0

    for caracter in palabra:
        if caracter in vocales:
            contarVocales += 1  # Este espacio es la clave

    print(f"la palabra {palabra} contiene esta cantidad de vocales {contarVocales}")

def contarVocales():
    palabra = input("Ingrese una palabra: ")
    vocales(palabra)

'''
Ejercicio 3
Crear una función que reciba una lista de nombres y 
muestre únicamente aquellos que tengan más de 5 letras.
'''
def nombres(listaNombres):
    for i in range(len(listaNombres)):
        if len(listaNombres[i]) > 5:
            print(f"\nEstos nombres tienen más de 5 letras\n{listaNombres[i]}")  

def nombres5Letras():
    listaNombres = []
    Cnombre = int(input("Ingrese la cantidad de nombres:\n"))
    for i in range(Cnombre):
        nombre = input("Ingrese los nombres:\n")
        listaNombres.append(nombre)
    nombres(listaNombres)

'''
Ejercicio 4
Crear una función que reciba una lista de notas (números decimales), 
calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
'''
def sacarPromedio(notas):
    cantidadNotas = len(notas)
    sumaNotas = sum(notas)
    promedio = sumaNotas / cantidadNotas
    
    if promedio >= 4.0:
        print(f"Su promedio de notas es de {promedio}\nEstas Aprobado!")
    else:
        print(f"Su promedio de notas es {promedio}\nEstas Reprobado!")

def notas():
    cantidadNotas = int(input("Cuantas notas quiere ingresar?\n"))
    notas = []
    for i in range(cantidadNotas):
        nota = float(input("Ingrese las notas:\n"))
        notas.append(nota)
    sacarPromedio(notas)
        
        
'''
Ejercicio 5 
Crear una función que reciba una lista de precios de productos y 
aplique un descuento del 10%, mostrando el valor original y el nuevo valor.
'''

def descuento(valor):
    sumaLista = sum(valor)
    precioInicial = sumaLista
    descuento = sumaLista * (90 / 100)
    print(f"El precio inical era de {precioInicial} y el precio final de {descuento}")

def valores():
    cantidadProductos = int(input("Ingrese la cantidad de productos que quiere ingresar:\n"))
    listaPrecios = []
    for i in range(cantidadProductos):
        valorProducto = float(input("Ingrese el valor de cada producto:\n"))
        listaPrecios.append(valorProducto)

    descuento(listaPrecios)


'''
Ejercicio 6
Crear una función que reciba un número entero y determine si es par o impar.
'''

def parImpar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

def numeroEntero():
    numero = int(input("Ingrese un número: "))
    parImpar(numero)
    
    
'''
Ejercicio 7
Crear una función que reciba una lista de edades y
muestre cuántas personas son mayores de edad (18 años o más).
'''

def mayorEdad(edades):
    contadorMayoresEdad = 0
    for i in edades:
        if i >= 18:
            contadorMayoresEdad += 1
    print(f"Estas cantidad de personas son mayores de edad {contadorMayoresEdad}")

def edad():
    cantidadEdades = int(input("Cuantas edades quieres ingresar?\n"))
    listaEdades = []
    for i in range(cantidadEdades):
        edades = int(input("Ingrese las edades:\n"))
        listaEdades.append(edades)
    mayorEdad(listaEdades)


'''
Ejercicio 8
Crear una función que reciba una lista de palabras y 
permita buscar cuántas veces aparece una palabra específica ingresada por el usuario.
'''

def palabraIgual(palabras):
    palabrasIguales = {}
    for test1 in range(len(palabras)):
        cantidadVeces = 0
        for test2 in range(len(palabras)):
            if palabras[test1] == palabras[test2]:
                cantidadVeces += 1
        palabrasIguales[palabras[test1]] = cantidadVeces
    print(palabrasIguales)

def palabras():
    cantidadPalabras = int(input("Cuantas palabras quiere ingresar?\n"))
    listaPalabras = []
    for i in range(cantidadPalabras):
        palabra = input("Ingrese la palabra:\n")
        listaPalabras.append(palabra)
    palabraIgual(listaPalabras)

'''
Ejercicio 9
Crear una función que reciba una lista de números y 
genere una nueva lista que contenga únicamente los números positivos.
'''

def numerosPositivos(listaNumeros):
    nuevaListaNumeros = []
    for i in listaNumeros:
        if i > 0:
            nuevaListaNumeros.append(i)
    print(f"Esta es la nueva lista de números enteros positivos\n{nuevaListaNumeros}")

def numeros():
    cantidadNumeros = int(input("Cuantos números quiere ingresar?\n"))
    listaNumeros = []
    for i in range(cantidadNumeros):
        numero = int(input("Ingrese cualquier número(positivo o negativo):\n"))
        listaNumeros.append(numero)
    numerosPositivos(listaNumeros)


'''
Ejercicio 10
Crear una función que reciba una lista de productos 
(utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades.
'''

def productos():
    pass

continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-10) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        mayorMenor()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2:")
        contarVocales()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        nombres5Letras()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4")
        notas()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5")
        valores()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6")
        numeroEntero()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7")
        edad()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8")
        palabras()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9")
        numeros()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10")
        
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no valida")