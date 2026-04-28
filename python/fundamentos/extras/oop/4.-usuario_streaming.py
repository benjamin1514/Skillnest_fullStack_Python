'''
📄 Crea un archivo de Python llamado usuario_streaming.py.

🗂️ Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
🧪 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces.
'''

# Todos los valores que se deban registrar debe ser con input
# Añadir un menu while para mostrar

class UsuarioStreaming:
    def __init__(self, nombre, email, suscripcion="Gratis"):
        self.nombre = nombre
        self.email = email
        self.suscripcion = suscripcion
        self.lista_reproduccion = []


    def agregar_a_lista(self, titulo):
        """Agrega un contenido a la lista de reproducción del usuario."""
        self.lista_reproduccion.append(titulo)
        print(f"Titulo {titulo} agregado")

    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        if titulo in self.lista_reproduccion:
            print(f"El usuario {self.nombre} esta viendo '{titulo}'")
        else:
            print(f"Titulo no encontrado {titulo}")


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        antigua = self.suscripcion
        self.suscripcion = nueva_suscripcion
        print(f"Suscripción cambió de {antigua} a {nueva_suscripcion}")


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Suscripcion: {self.suscripcion}")
        if len(self.lista_reproduccion) == 0:
            print("La lista de reproducciones esta vacía.")
        else:
            print(f"Lista de reproduccion: \n- {"\n".join(self.lista_reproduccion)}")
    
    
benja = UsuarioStreaming("Benjamin", "Benjamin@gmail.com")
randy = UsuarioStreaming("Randy", "randy@gmail.com")
tete = UsuarioStreaming("Tete", "tete@gmail.com")

nombres = [benja, randy, tete] # Guardo las instancias en un array


continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        print("Usuarios disponibes") 
        for i in range(len(nombres)):
            print(f"{i}: {nombres[i].nombre}")
        # Muestro los usuarios disponibles 
        indice = int(input("Selecciona el número del usuario (0, 1 o 2): "))
        usuario_seleccionado = nombres[indice]
        # Aqui para la elección de la instancia elegia por su indice en el array
        benjaM = int(input(f"Cuantos titulos quiere agregar a {usuario_seleccionado.nombre}\n"))
        for i in range(benjaM):
            tituloAgregado = input("Que titulo quieres agregar?\n")
            usuario_seleccionado.agregar_a_lista(tituloAgregado)
            
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        print("Usuarios disponibes") 
        for i in range(len(nombres)):
            print(f"{i}: {nombres[i].nombre}")
        # Muestro los usuarios disponibles 
        indice = int(input("Selecciona el número del usuario (0, 1 o 2): "))
        usuario_seleccionado = nombres[indice]
        # Aqui para la elección de la instancia elegia por su indice en el array
        tipoSuscripcion = input(f"Que tipo de suscripción tienes {usuario_seleccionado.nombre} (Gratuita)")
        cambiarSuscripcion = input(f"A cual tipo de suscripción quieres cambiar?\n")
        usuario_seleccionado.cambiar_suscripcion(cambiarSuscripcion)
    elif opcion == "4":
        print("\nEjecutando ejercicio 4")
        
    elif opcion == "5":
        pass
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no valida")