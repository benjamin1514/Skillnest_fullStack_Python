# Esta es la sintaxis para crear una clase llamada Usuario:
# Creación de la clase usuario 
class Usuario:
    def __init__(self): # Constructor 
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0
                                    
# Y para crear una nueva instancia de nuestra clase se vería como: 
# Instancias de una clase 
miyagi = Usuario()

daniel = Usuario()

benjamin = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido)
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)


# Ahora establezcamos valores distintos para nuestras instancias:
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "danielLarusso@gmail.com"
daniel.limite_credito = 1000000
daniel.saldo_pagar = 300000
print(daniel.nombre) #Imprime: Daniel
print(daniel.apellido)
print(daniel.email)
print(daniel.limite_credito)
print(daniel.saldo_pagar)

# Valores a nueva instancia 

benjamin.nombre = "Benjamin"
benjamin.apellido = "Delgado"
benjamin.email = "benjamin@gmail.com"
benjamin.limite_credito = 100000
benjamin.saldo_pagar = 0
# Imprimir nombre de cada instancia 
print(benjamin.nombre) #Imprime: Benjamin
print(daniel.nombre) 
print(miyagi.nombre)
print(benjamin.apellido)
print(benjamin.email)
print(benjamin.limite_credito)
print(benjamin.saldo_pagar)

