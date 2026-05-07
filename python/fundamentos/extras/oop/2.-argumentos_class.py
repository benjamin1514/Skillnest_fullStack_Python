# Pasar argumentos 
'''
Para poder personalizar nuestras instancia vamos a pasar algunos argumentos al método __init__ 
y que de esta manera podamos asignarle a los atributos los valores correspondientes.
'''

class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        
# Creación de instancias 
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 300000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 200000, 10000)
benjamin = Usuario("Benjamin", "Delgado", "benjamin@gmail.com", 200000, 0)
# Imprimimos los valores 
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

# Imprime valores de daniel 
print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

print(benjamin.nombre) #Imprime: Daniel
print(benjamin.apellido)
print(benjamin.email)
print(benjamin.limite_credito)
print(benjamin.saldo_pagar)

#--- tarea rapida

'''
Crear una clase Estudiantes, y asignarle lo siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
'''

class Estudiantes: 
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac
        
randy = Estudiantes("22898879-0", "Randy", "Cortines", "Programación", "28-11-2008")
tete = Estudiantes("22633816-0", "Elizabeth", "Cornejo", "Programacion", "30-01-2008")
benja = Estudiantes("22926226-2", "Benjamin", "Delgado", "Programación", "07-01-2009")

print(f"El nombre es: {randy.nombre} {randy.apellido} y la especialidad es {randy.especialidad}")
print(f"El nombre es: {tete.nombre} {tete.apellido} y la especialidad es {tete.especialidad}")
print(f"El nombre es: {benja.nombre} {benja.apellido} y la especialidad es {benja.especialidad}")