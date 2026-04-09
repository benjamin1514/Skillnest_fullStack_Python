'''
1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos.
'''
def numerosDinamicos():
    numerosPares = int(input("Ingrese cantidad de números pares que quiera ver: "))
    pares = []

    for i in range(1, ( numerosPares * 2 ) + 1):
        if i % 2 == 0: 
            pares.append(i)
        print(f"Mostrando pares: {pares}")
    

'''
2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
'''
def edadMin(): 
    edad = int(input("Ingrese su año de nacimiento: "))
    año = 2026 - edad
    if año >= 18:
        print("Eres mayor de edad")
    elif año < 18 and año > 0: 
        print(f"Tienes {año} y te faltan {18 - edad}")
    else:
        print("Ingrese un valor válido")

'''
3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. 
Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, 
el descuento aplicado y el total final.
'''
def descuento():
    precio = int(input("Ingrese el valor del producto: "))
    if precio >= 100000:
        descuento = precio * 0.85
        print(f"el precio del producto con el descuento es {descuento}")
    else:
        print("No tiene descuento")

'''
4. Clasificador de Números
Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar,
Negativo-Par, Negativo-Impar o Cero.
'''

def clasificarNumeros():
    numero = int(input("Ingrese un número, negativo o positivo: "))

    for i in range(1): 
        if numero > 0 and numero % 2 == 0:
            print(f"{numero} es par positivo")
        elif numero > 0 and numero % 2 == 1:
            print(f"{numero} es impar positivo")
        elif numero < 0 and numero % 2 == 0:
            print(f"{numero} es par negativo")
        elif numero < 0 and numero % 2 == 1:
            print(f"{numero} es impar negativo")
        else:
            print("Es cero")
        


'''
5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
pero solo muestra los resultados que sean múltiplos de 3.
'''
def multiplicarMultiplosTres():
    numero = int(input("Ingrese un número: "))

    for i in range(1, 12 + 1,1):
        if numero * i % 3 == 0:
            print(f"{numero} * {i} = {numero * i}")
            
            

'''
6. Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume.
El ciclo debe terminar cuando el usuario ingrese un número negativo. 
Al final, muestra la suma total (sin incluir el negativo).
'''

def sumatoriaCentinal():
    total = 0
    num = int(input("Indique cuantos números quiere sumar: "))
    for i in range(num):
        if numeros > 0:
            numeros = int(input("Coloque los números: "))
            total += numeros
            print(total)
        elif numeros < 0:
            print("Es negativo")
            break
        else:
            print("No es un número")
        

'''
7. Contador de Vocales
Pide al usuario una frase o palabra. 
Utiliza un bucle para recorrer la cadena y contar cuántas vocales tiene en total.
'''

def contadorVocales():
    palabra = input("Indique una palabra: ")
    vocales = "aeiouáéíóú"
    for a in a:
        print(i, vocales[i])


continuar = True

while continuar:
    print("\n--- ejercicios python---")
    print("--- 1.- Ejercicio 1---")
    print("--- 2.- Ejercicio 2---")
    print("--- 3.- Ejercicio 3---")
    print("--- 4.- Ejercicio 4---")
    print("--- 5.- Ejercicio 5---")
    print("--- 6.- Ejercicio 6---")
    print("--- 7.- Ejercicio 7---")
    print("--- 8.- Ejercicio 8---")
    print("--- 9.- Ejercicio 9---")
    print("--- 10.- Ejercicio 10---")
    print("--- 11.- Ejercicio 11---")
    print("--- 12.- Ejercicio 12---")
    print("--- 13.- Ejercicio 13---")
    print("--- 14.- Ejercicio 14---")
    print("--- 15.- Ejercicio 15---")
    opcion = input("\n---- Elige una opción: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        numerosDinamicos()
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        edadMin()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        descuento()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4")
        clasificarNumeros()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5")
        multiplicarMultiplosTres()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6")
        sumatoriaCentinal()
    elif opcion == "7":
        print("\nEjecutando ejercicio 7")
        contadorVocales()
    elif opcion == "8":
        print("\nEjecutando ejercicio 8")
        print()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9")
        print()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10")
        print()
    elif opcion == "11":
        print("\nEjecutando ejercicio 11")
        print()
    elif opcion == "12":
        print("\nEjecutando ejercicio 12")
        print()
    elif opcion == "13":
        print("\nEjecutando ejercicio 13")
        print()
    elif opcion == "14":
        print("\nEjecutando ejercicio 14")
        print()
    elif opcion == "15":
        print("\nEjecutando ejercicio 15")
        print()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else: 
        print("Opción no válida, intente otra vez")