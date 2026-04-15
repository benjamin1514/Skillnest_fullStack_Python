"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)

def generadorNiveles(): 
    for i in range(1, 100 + 1):
        print(f"Nivel: {i}")

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)

def pares():
    limite = 500
    
    for i in range(2, limite + 1, 2):
        if i % 2 == 0:
            print(i)


# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)

def trampaEmoji():
    for i in range(1, 100 + 1):
        if i % 10 == 0:
            print("Es divisible por 10")
        elif i % 5 == 0:
            print("Es divisible por 5")
        else:
            print(i)


# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí)

def sumaPares():
    sumaPares = 0
    limite = 500000
    
    for i in range(1, limite + 1):
        if i % 2 == 0:
            sumaPares += i
    print(f"La suma de los números pares hasta {limite} es: {sumaPares}")



# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)

def retrocesoTemporal():
    for i in range(2024, 0, -3):
        print(f"Año {i}")


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)

def contadorDinamico():
    inicio = 7
    fin = 30
    salto = 4

    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10


continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        generadorNiveles()
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        pares()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        trampaEmoji()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4")
        sumaPares()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5")
        retrocesoTemporal()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6")
        contadorDinamico()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else: 
        print("Opción no válida, intente otra vez")