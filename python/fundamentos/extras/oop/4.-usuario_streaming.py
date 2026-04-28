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


    def ver_contenido(self, titulo):
        """Simula que el usuario reproduce un contenido."""
        pass


    def cambiar_suscripcion(self, nueva_suscripcion):
        """Cambia el tipo de suscripción del usuario."""
        pass


    def mostrar_info_usuario(self):
        """Muestra la información del usuario y su lista de reproducción."""
        pass
    
    
benja = UsuarioStreaming("Benjamin", "Benjamin@gmail.com")
randy = UsuarioStreaming("Randy", "randy@gmail.com")

benja.agregar_a_lista(input("Quieres agregar algun titulo?\n"))

continuar = True

while continuar:
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1:")
        print(benja.lista_reproduccion)
    elif opcion == "2":
        print("\nEjecutando ejercicio 1:")
        
    elif opcion == "3":
        print("\nEjecutando ejercicio 3")
        
    elif opcion == "4":
        print("\nEjecutando ejercicio 4")
        
    elif opcion == "5":
        pass
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no valida")