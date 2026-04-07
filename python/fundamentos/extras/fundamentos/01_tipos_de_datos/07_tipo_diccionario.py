# Diccionario

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
print(estudiante["nombre"]) #Imprime: Gonzalo

# Acceder y modificar valores
estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente

estudiante["nombre"] = "Benjamin"
print(estudiante["nombre"])
#Diccionario paises
paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["ARG"] = "Argentina"



# Verificar la existencia de una clave
'''
¿Notaste que utilizamos la misma sintaxis para crear un nuevo elemento y modificar el valor de un elemento? 
Algunas veces necesitaremos verificar si existe alguna clave en 
el diccionario para saber si estamos agregando un valor inicial o bien reemplazando un valor existente.
'''

if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"

# Remover valores
# Tenemos dos maneras de eliminar un elemento del diccionario:
valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print(f"Valor removido: {valor_removido}")
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

print(paises)

# Sintaxis multi-línea 

'''
Puedes escribir los pares de clave-valor de un diccionario en múltiples 
líneas para leerlo de una manera más fácil. 
Esto es muy útil sobre todo en diccionarios más largos. Por ejemplo el siguiente diccionario:
'''

pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

# Puede ser escrito de esta manera:

pintor = {
    "nombre": "Frida Kahlo",
    "pais": "México",
    "fecha_nacimiento": "6 de julio de 1907"
}

# Diccionarios anidados

'''
Como mencionamos anteriormente, los valores que podemos utilizar 
para los diccionarios pueden contener listas,
tuplas e inclusive otros diccionarios.
'''

escuela = {
    "nombre": "Coding Dojo LATAM",
        "profesores": [
            {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
            {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
            {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}

print(escuela["profesores"])

#  Funciones y métodos integrados

# len(diccionario): regresa el tamaño de un diccionario .
# str(diccionario): crea una representación de cadena (imprimible) de un diccionario.
# type(diccionario): regresa el tipo de la variable. Si la variable es un diccionario, devolverá un tipo de dict.

'''
Veamos también algunos métodos de los diccionarios. 
La sintaxis puede ser dict.method(tu_diccionario) o tu_diccionario.method(), 
donde method es el método a utilizar.
'''

# .clear(): elimina todos los elementos del diccionario
#  .copy(): regresa una copia del diccionario
# get(clave, default=None): regresa el valor establecido para una clave o None si la clave no se encuentra en el diccionario.
# .has_key(clave): regresa verdadero (True) si la clave proporcionada está disponible en el diccionario; de lo contrario, devuelve False.
# .items(): regresa una lista de pares de tuplas (clave, valor) del diccionario.
# .keys(): regresa una lista de claves de diccionario.
# .update(pares_actualizar): agrega y actualiza los pares clave-valor del diccionario enviado al diccionario existente.
# .values(): regresa una lista de valores del diccionario.