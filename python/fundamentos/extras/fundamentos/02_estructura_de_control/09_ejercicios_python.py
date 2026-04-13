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
    palabra = input("Indique una palabra: ").lower()
    vocales = "aeiouáéíóú"
    contarVocales = 0

    for caracter in palabra:
        if caracter in vocales:
            contarVocales += 1  # Este espacio es la clave

    print(f"La frase {palabra} contiene {contarVocales} vocales")
    
'''
8. Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
'''

def validar():
    contraseña = "hola1234"
    for i in range(3):
        usuario = input("Intente adivinar la contraseña(3 Intentos):")
        if usuario == contraseña:
            print("Adivinaste la contraseña!")
            return
        else:
            print("Contraseña incorrecta! intente denuevo")
    print("No adivinaste la contraseña")


'''
9. Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. 
Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados.
'''

def registroNombres():
    nombre = []
    for i in range(5):
        user = input("Ingrese 5 nombres: ")
        nombre.append(user)
    print(nombre)
    
'''
10. Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.
'''

def promedio(): 
    cantidadNotas = int(input("Ingrese la cantidad de notas: "))
    arrNotas = []
    notasSuma = 0
    for i in range(cantidadNotas):
        ingresarNotas = float(input("Ingrese las notas: "))
        arrNotas.append(ingresarNotas)
        notasSuma += ingresarNotas
    promedio = notasSuma / cantidadNotas
    print(f"{ingresarNotas}, \n{promedio} \n{max(arrNotas)} {min(arrNotas)} {arrNotas}")


'''
11. Filtro de Arreglos
Dado un arreglo de números generado por el usuario, 
crea un nuevo arreglo que contenga solo los números que sean mayores a 50. Muestra ambos arreglos.
'''

def filtroArreglo():
    cantidad = int(input("¿Cuantos números desea ingresar? "))
    mayor50 = []
    nUser = []
    for i in range(1, cantidad + 1):
        arrayUsuario = int(input("Ingrese un número: "))
        if arrayUsuario > 50:
            mayor50.append(arrayUsuario)
        else:
            nUser.append(arrayUsuario)
    print(f"Valores ingresados por el ususario: {nUser} \nValores mayor a 50: {mayor50}")
    
'''
12. Buscador de Elementos
Crea una lista de 10 ciudades.
Pide al usuario que ingrese el nombre de una ciudad y 
el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
'''

def buscadorCiudades():
    ciudades = ["Nairobi", "Tokio", "Santiago", "Lima", "Caracas", "Rio", "Berlin", "Seul", "Buenos aires"]
    ciudad = input("Ingrese el nombre de la ciudad(con mayuscula al principio): ").capitalize()
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
        print(f"Tu ciudad esta en el arreglo, en la posición {esta}")
    else:
        print("Tu ciudad no esta")


'''
13. Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. 
Permite al usuario ingresar 3 productos con sus precios. 
Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
'''

def inventario(): 
    

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
        validar()
    elif opcion == "9":
        print("\nEjecutando ejercicio 9")
        registroNombres()
    elif opcion == "10":
        print("\nEjecutando ejercicio 10")
        promedio()
    elif opcion == "11":
        print("\nEjecutando ejercicio 11")
        filtroArreglo()
    elif opcion == "12":
        print("\nEjecutando ejercicio 12")
        buscadorCiudades()
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