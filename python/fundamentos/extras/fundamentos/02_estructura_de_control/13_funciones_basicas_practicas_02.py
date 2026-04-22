import os

# Calcula experiencia
def multiplica_por_2(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado

def ejercicio1(): 
    resultado = multiplica_por_2(5)
    print(f"El resultado es: {resultado}")
# Debe retornar: [0, 2, 4, 6, 8, 10]

def suma_y_resta(sumaResta):
    suma = sumaResta[0] + sumaResta[1]
    resta = sumaResta[0] - sumaResta[1]
    print(suma)
    return resta    

def ejercicio2():
    resta = suma_y_resta([120, 115])
    print(f"Resta : {resta}")
    
#Analiza publicaciones
# Imprime: 235 y retorna: 5


# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"Total = {total}, longitud = {longitud}")
    return resultado
    
    
def ejercicio3(): 
    resultado = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado es: {resultado}")

# Suma total = 25, longitud = 4, debe retornar: 21

def valores_multiplicados_segundo(multiplicar):
    if len(multiplicar) < 2:
        print(len(multiplicar))
        return []
    
    valores_multiplicador = multiplicar[1]
    print(len(multiplicar))
    
    nueva_lista = []
    for i in multiplicar:
        nueva_lista.append(i * valores_multiplicador)
    return nueva_lista

def ejercicio4(): 
    resultado = valores_multiplicados_segundo([100, 3, 50, 20])
    result = valores_multiplicados_segundo([100])
    
    print(f"{resultado}")
    print(f"{result}")
# Ajusta visualizaciones
# Imprime: 4 y retorna: [300, 9, 150, 60]
# print()
# Imprime: 1 y retorna: []

def valor_multiplicado_longitud(valor, longitud):
    resultado_multiplicacion = valor * longitud
    lista = []
    for i in range(longitud):
        lista.append(resultado_multiplicacion)
    return lista
        
        
def ejercicio5():
    lista = valor_multiplicado_longitud(5, 2)
    print(f"{lista}")
    listas = valor_multiplicado_longitud(7, 5)
    print(f"{listas}")
# Genera precio fijo
# print()
# Debe retornar: [10, 10]
#print()
# Debe retornar: [35, 35, 35, 35, 35]


def limpiarConsola():
    os.system('cls')

continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-5) (0 para salir) =")

    if opcion == "1":
            limpiarConsola()
            print("\nEjecutando ejercicio 1:")
            print(multiplica_por_2(5))
    elif opcion == "2":
            limpiarConsola()
            print("\nEjecutando ejercicio 2:")
            ejercicio2()
    elif opcion == "3":
            limpiarConsola()
            print("\nEjecutando ejercicio 3")
            ejercicio3()
    elif opcion == "4":
            limpiarConsola()
            print("\nEjecutando ejercicio 4")
            ejercicio4()
    elif opcion == "5":
            limpiarConsola()
            print("\nEjecutando ejercicio 5")
            ejercicio5()
    elif opcion == "0":
            limpiarConsola()
            print("Saliendo...")
            continuar = False
    else: 
            print("Opción no válida, intente otra vez")