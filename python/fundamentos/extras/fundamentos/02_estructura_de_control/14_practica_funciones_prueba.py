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
            print(listaNombres[i])  

def nombres5Letras():
    listaNombres = ["Benjamin", "Randy", "Akon", "Marcelo"]
    nombres(listaNombres)

'''
Ejercicio 4
Crear una función que reciba una lista de notas (números decimales), 
calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0).
'''
def sacarPromedio():
    pass



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
        valorProducto = int(input("Ingrese el valor de cada producto: "))
        listaPrecios.append(valorProducto)

    descuento(listaPrecios)



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
        
    elif opcion == "5":
        print("\nEjecutando ejercicio 5")
        valores()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6")
        
    elif opcion == "7":
        print("\nEjecutando ejercicio 7")
        
    elif opcion == "8":
        print("\nEjecutando ejercicio 8")
        
    elif opcion == "9":
        print("\nEjecutando ejercicio 9")
        
    elif opcion == "10":
        print("\nEjecutando ejercicio 10")
        
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no valida")