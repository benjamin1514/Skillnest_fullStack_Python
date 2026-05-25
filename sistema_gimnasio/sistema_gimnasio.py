'''
Escenario 2 — Sistema de Gimnasio
Un gimnasio necesita un sistema para administrar sus clientes, entrenadores y planes de entrenamiento. 
El sistema permitirá organizar la información de los usuarios y sus actividades.
Clases sugeridas
Cliente
Entrenador
PlanEntrenamiento
Métodos sugeridos
Clase Cliente
mostrar_cliente()
actualizar_telefono()
Clase Entrenador
mostrar_entrenador()
asignar_cliente()
Clase PlanEntrenamiento
mostrar_plan()
modificar_duracion()
'''
    
class PlanEntrenamiento:
    def __init__(self, nombre_plan, duracion_plan):
        self.nombre_plan = nombre_plan
        self.duracion_plan = duracion_plan
        
    def mostrar_plan(self):
        self.nombre_plan
        
        pass
    
    def modificar_duracion():
        pass
    

plan = PlanEntrenamiento("Fuerza", "4 Semanas")
plan2 = PlanEntrenamiento("Pilometria", "2 Meses")
plan3 = PlanEntrenamiento("Pierna", "2 Semanas")

class Cliente: 
    def __init__(self,nombre, numero, correo, plan):
        self.nombre = nombre
        self.numero = numero
        self.correo = correo
        self.plan = plan
        
        def mostrar_cliente():
            pass
        
        def actualizar_telefono():
            pass
        
    
cliente1 = Cliente("José", "932494323", "José@gmail.com")
cliente2 = Cliente("Martina", "932674532", "Martina@gmail.com")
cliente3 = Cliente("Luciano", "932895643", "Luciano@gmail.com")

Cliente.mostrar_cliente()
Cliente.actualizar_telefono()

class Entrenador:
    def _init_(self, nombre_entrenador, numero_entrenador, correo_entrenador, clases_asginadas):
        self.nombre_entrenador = nombre_entrenador
        self.numero_entrenador = numero_entrenador
        self.correo_entrenador = correo_entrenador
        self.clases = clases_asginadas
        
    def mostrar_entrenador():        
        pass

    def asignar_cliente():       
        pass

entrenador1 = Entrenador("Jose")
    
PlanEntrenamiento.mostrar_entrenador()
PlanEntrenamiento.asignar_cliente()



continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        ()
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        ()    
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        ()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else: 
        print("Opción no válida, intente otra vez")


