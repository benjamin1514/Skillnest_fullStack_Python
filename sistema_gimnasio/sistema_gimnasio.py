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
        print(f"{self.nombre_plan} | {self.duracion_plan}")
        
    
    def modificar_duracion(self):
        cambio = input("A cuanto tiempo quieres cambiar la duración?\n")
        self.duracion_plan = cambio
        
        print(f"El plan de {self.nombre_plan} cambio su tiempo a {cambio} Semanas")
    


plan1 = PlanEntrenamiento("Fuerza", "4 Semanas")
plan2 = PlanEntrenamiento("Pilometria", "2 Semanas")
plan3 = PlanEntrenamiento("Pierna", "2 Semanas")





class Cliente: 
    def __init__(self,nombre, numero, correo, cambiar_numero):
        self.nombre = nombre
        self.numero = numero
        self.correo = correo
        self.cambiar_numero = cambiar_numero
        
    def mostrar_cliente(self):
        print(f"Nombre: {self.nombre} Número: {self.numero} Correo: {self.correo}")
    
    def actualizar_telefono(self):
        #self.cambiar_numer = input(f"Cambia el numero:\n")     
        # self.cambiar_num = cambiar_numero 
        pass
#cliente1 = Cliente("José", "932494323", "José@gmail.com")
#cliente2 = Cliente("Martina", "932674532", "Martina@gmail.com")
# cliente3 = Cliente("Luciano", "932895643", "Luciano@gmail.com")



class Entrenador:
    def _init_(self, nombre_entrenador, numero_entrenador, correo_entrenador, clases_asignadas):
        self.nombre_entrenador = nombre_entrenador
        self.numero_entrenador = numero_entrenador
        self.correo_entrenador = correo_entrenador
        self.clases = clases_asignadas
        
    def mostrar_entrenador():        
        pass

    def asignar_cliente():       
        pass

    
Entrenador.mostrar_entrenador()
Entrenador.asignar_cliente()



continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        plan1.mostrar_plan()
        plan2.mostrar_plan()
        plan3.mostrar_plan()
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        print("1\n2\n3")
        plan = input("Ingrese a cual quiere cambiar\n")
        if plan == "1":
            plan1.modificar_duracion()
        elif plan == "2":
            plan2.modificar_duracion()
        elif plan == "3":
            plan3.modificar_duracion()
        else:
            print("Ingrese una opción Valida.")
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        ()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else: 
        print("Opción no válida, intente otra vez")


