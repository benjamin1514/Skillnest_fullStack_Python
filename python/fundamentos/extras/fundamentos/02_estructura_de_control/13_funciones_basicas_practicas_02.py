import os

# Calcula experiencia
def multiplica_por_2(num):
    resultado = []
    for i in range(num + 1):
        resultado.append(i * 2)
    return resultado

# print(multiplica_por_2(5))
# Debe retornar: [0, 2, 4, 6, 8, 10]

def suma_y_resta(sumaResta):
    suma = sumaResta[0] + sumaResta[1]
    resta = sumaResta[0] - sumaResta[1]
    print(suma)
    return resta    
# Analiza publicaciones
# print(suma_y_resta([120, 115]))
# Imprime: 235 y retorna: 5


# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    
    return resultado
    
# print(sumatoria_menos_longitud([10, 5, 3, 7]))
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
# print(valores_multiplicados_segundo([100, 3, 50, 20]))
# Ajusta visualizaciones
# Imprime: 4 y retorna: [300, 9, 150, 60]
# print(valores_multiplicados_segundo([100]))
# Imprime: 1 y retorna: []

def valor_multiplicado_longitud(valor, longitud):
    resultado_multiplicacion = valor * longitud
    lista = []
    for i in range(longitud):
        lista.append(resultado_multiplicacion)
    return lista
        
# Genera precio fijo
# print(valor_multiplicado_longitud(5, 2))
# Debe retornar: [10, 10]
#print(valor_multiplicado_longitud(7, 5))
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
            print("\nEjecutando ejercicio 1:")
            print(suma_y_resta([120, 115]))
    elif opcion == "3":
            limpiarConsola()
            print("\nEjecutando ejercicio 3")
            print(sumatoria_menos_longitud([10, 5, 3, 7]))
    elif opcion == "4":
            limpiarConsola()
            print("\nEjecutando ejercicio 4")
            print(valores_multiplicados_segundo([100, 3, 50, 20]))
            print(valores_multiplicados_segundo([100]))
    elif opcion == "5":
            limpiarConsola()
            print("\nEjecutando ejercicio 5")
            print(valor_multiplicado_longitud(5, 2))
            print(valor_multiplicado_longitud(7, 5))
    elif opcion == "0":
            limpiarConsola()
            print("Saliendo...")
            continuar = False
    else: 
            print("Opción no válida, intente otra vez")