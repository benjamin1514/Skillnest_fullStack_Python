''' Define la clase SuscripcionStreaming, que debe incluir:

Atributos:
usuario (nombre del usuario asociado a la suscripción)
tipo_suscripcion (Gratis, Estándar, Premium)
costo_mensual (según el tipo de suscripción)
saldo_pendiente (monto acumulado que debe pagar el usuario)
Métodos:
realizar_pago(self, monto) reduce el saldo pendiente según el monto pagado.
cambiar_suscripcion(self, nuevo_tipo) cambia el tipo de suscripción y ajusta el costo mensual.
ver_contenido_exclusivo(self) permite el acceso a contenido según el tipo de suscripción. La suscripción “Gratis” no tiene acceso a contenido exclusivo.
mostrar_info_suscripcion(self) muestra el estado actual de la suscripción del usuario.
Realizar las siguientes pruebas con instancias:

Crea 3 usuarios con diferentes tipos de suscripción.
Haz que el primer usuario intente ver contenido exclusivo, mejore su suscripción y pague su saldo.
Haz que el segundo usuario vea contenido exclusivo, cambie su suscripción a Premium y pague dos veces.
Haz que el tercer usuario intente pagar una cantidad menor a su saldo pendiente y vea contenido exclusivo.
'''


class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0, "Estándar": 5.99, "Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        """Reduce el saldo pendiente según el monto pagado."""
        self.saldo_pendiente -= monto
        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0
        print(f"{self.usuario} pagó ${monto}")

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.costo_mensual
            print(f"{self.usuario} cambió a suscripción {nuevo_tipo}")
        else:
            print("Tipo de suscripción no válido")

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""
        if self.tipo_suscripcion == "Premium":
            print("Puedes ver contenido exclusivo Premium")
        elif self.tipo_suscripcion == "Estándar":
            print("Puedes ver contenido estándar")
        else:
            print("La cuenta Gratis no tiene contenido exclusivo")

    def mostrar_info_suscripcion(self):
        """Muestra la información de la suscripción del usuario."""
        print("INFORMACIÓN")
        print(f"Usuario: {self.usuario}")
        print(f"Tipo: {self.tipo_suscripcion}")
        print(f"Costo mensual: ${self.costo_mensual}")
        print(f"Saldo pendiente: ${self.saldo_pendiente}")
        


usuario1 = SuscripcionStreaming("Daniel")
usuario2 = SuscripcionStreaming("Jesus", "Premium")
usuario3 = SuscripcionStreaming("Zárate", "Estándar")


usuario1.mostrar_info_suscripcion()

usuario2.realizar_pago(5)
usuario2.mostrar_info_suscripcion()

usuario3.ver_contenido_exclusivo()

usuario1.cambiar_suscripcion("Premium")
usuario1.mostrar_info_suscripcion()