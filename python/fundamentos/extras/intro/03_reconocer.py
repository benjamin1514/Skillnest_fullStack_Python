"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random # Importacion de libreria para procesos aleatorios 


nombre = "Frida Kahlo" # se crea una variable nombre es tipo string y se le asigna valor
print(type(nombre)) # type = metodo de python para mostrar el tipo de dato de la variable 
print(len(nombre)) # len = metodo que cuenta el largo de la variable y lo devuelve a la consola


edad = 25 # se crea una variable edad tipo Int y se le asigna valor 


if edad < 18: # se crea condición if y dice si edad es menor 18 pasa
    print("Eres menor de edad.") # Muestra en la consola el mensaje
elif edad == 18:  # Condicion else if(elif) que dice si es igual que 18
    print("Tienes 18 años.") # Muestra en la consola el mensaje
else: # cierre de condicion (sino se cumplenn las condiciones anteriores)
    print("Eres mayor de edad.") # muestra el mensaje en la consola 


frutas = ["manzana", "pera", "fresa"]  # Se crea un array(arreglo) con 2 posiciones 
print(frutas[0]) # Muestra la posicion 0 del array(arreglo)
frutas[0] = "banana" # A la posicion 0 se le asigna "Banana"
frutas.append("uva") # Se le incerta al final al arreglo ultima posición
frutas.remove("pera") # Se remueve "pera" del arreglo(array)


dimensiones = (200, 50) # Se crea una variable tipo tupla con dos valores asignados, variable inmutable
print(dimensiones[0]) # Muestra la primera posicion de la tupla 


persona = { # Se crea una variable tipo diccionario
    "nombre": "Carlos", # Se le asigna a "nombre": "Carlos" 
    "edad": 30 # Se le asigna a "edad": 30
}
print(persona["nombre"]) # Imprime el valor del item ejemplo: Carlos
persona["edad"] = 31 # Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" # Se agrega un nuevo item con un valor
del persona["ciudad"] # Se elimina el item completo (ciudad)


for i in range(5): # Se crea un bucle for de un rango hasta 5 y inicia en 0 a 5
    # print(i)
    if i == 2: # Se crea una condicion if i == 2
        continue #  Continue ignora el proceso
    if i == 4: # se crea una condicion if i == 4
        break #  si i == 4 break hace que termine aqui mismo el bucle 
    print(i) # Imprime el valor de i en cada iteracion hasta 4


contador = 0 # Se crea una variable tipo num(Int) con un valor
while contador < 3: # Se crea un bucle while con una condicion contador < 3
    print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con f"" strign
    contador += 1 # Incrementa más uno en cada vuelta del bucle(iteración)


def saludar_usuario(nombre): # Se crea una funcion def(palara reservaba para crear una función en python) con un parametro
    return f"Hola, {nombre}" # Devuelve un valor de la función 


print(saludar_usuario("Francisca")) # Se imprime "Hola, Francisca" return de la función