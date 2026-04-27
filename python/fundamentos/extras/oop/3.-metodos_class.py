# Pero para esto, necesitamos que el método exista. ¡Vamos a crearlo!

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta e
    
    def aumentarCredito(self, aumento):
        self.limite_credito += aumento
        
    def cambiarCorreo(self, correo):
        self.email = correo






miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre} ${miyagi.saldo_pagar}")
segundaCompra = 300
miyagi.hacer_compra(segundaCompra)
print(f"Segunda compra de {miyagi.nombre} ${segundaCompra}") #Imprime: 350

print(f"Credito disponible {miyagi.limite_credito - miyagi.saldo_pagar}")

print(f"\nCompras de Daniel")
# Compras de daniel 
daniel.hacer_compra(45)
print(f"Primera compra de {daniel.nombre} ${daniel.saldo_pagar}") #Imprime: 45

print(f"Credito disponible {daniel.limite_credito - daniel.saldo_pagar}")

# Tarea 

'''
1.- Crear un nuevo metodo que permita aumentar el límite de crédito 
Imprimir el nuevo limite 
'''
miyagi.aumentarCredito(20000)
print(f"El nuevo limite de credito: {miyagi.limite_credito}")

'''
2.- Crear un nuevo método para cambiar el correo de la instancia 
mostrar el nuevo correo 
'''
miyagi.cambiarCorreo("benja@gmail.com")
print(f"El nuevo correo es: {miyagi.email}")