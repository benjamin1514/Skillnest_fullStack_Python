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
    
numerosDinamicos()
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
        
        
edadMin()
'''
3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. 
Si el total supera los $100, aplica un 15% de descuento. Muestra el subtotal, 
el descuento aplicado y el total final.
'''
def descuento():
    precio = int(input("Ingrese el valor del producto: "))


    for i in range(1): 
        if precio >= 100000:
            descuento = precio * 0.85
            print(f"el precio del producto con el descuento es {descuento}")
        else:
            print("No tiene descuento")

descuento()
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
        multiplicacion = numero % 3 == 0
        print(f"Numeros multiplos de 3 {numero}")
