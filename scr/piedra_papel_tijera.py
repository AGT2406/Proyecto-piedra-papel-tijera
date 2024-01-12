import random

# Definición de las opciones del juego
PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'

class IA:
    def __init__(self):
        # Lista de opciones del juego
        self.acciones_juego = [PIEDRA, PAPEL, TIJERAS]
        # Diccionario para almacenar las jugadas aprendidas por la IA
        self.jugadas_aprendidas = {}

    def obtener_accion_ia(self):
        # Si no hay jugadas aprendidas, iniciar siempre con papel
        if not self.jugadas_aprendidas:
            return PAPEL
        else:
            # Elegir la jugada basándose en las jugadas aprendidas
            jugada_mas_comun = max(self.jugadas_aprendidas, key=self.jugadas_aprendidas.get)
            if jugada_mas_comun == PIEDRA:
                return PAPEL
            elif jugada_mas_comun == PAPEL:
                return TIJERAS
            elif jugada_mas_comun == TIJERAS:
                return PIEDRA

    def actualizar_jugadas_aprendidas(self, jugada):
        # Actualizar el diccionario de jugadas aprendidas
        if jugada in self.jugadas_aprendidas:
            self.jugadas_aprendidas[jugada] += 1
        else:
            self.jugadas_aprendidas[jugada] = 1

def evaluar_juego(accion_usuario, accion_computadora, ia):
    print(f"\nTu elección: {accion_usuario}. La computadora eligió: {accion_computadora}")

    # Actualizar las jugadas aprendidas de la inteligencia artificial
    ia.actualizar_jugadas_aprendidas(accion_computadora)

    # Evaluar el resultado del juego
    if accion_usuario == accion_computadora:
        print(f"Ambos eligieron {accion_usuario}. ¡Empate!")

    elif accion_usuario == PIEDRA:
        if accion_computadora == TIJERAS:
            print("La piedra aplasta las tijeras. ¡Ganaste!")
        else:
            print("El papel cubre la piedra. ¡Perdiste!")

    elif accion_usuario == PAPEL:
        if accion_computadora == PIEDRA:
            print("El papel cubre la piedra. ¡Ganaste!")
        else:
            print("Las tijeras cortan el papel. ¡Perdiste!")

    elif accion_usuario == TIJERAS:
        if accion_computadora == PIEDRA:
            print("La piedra aplasta las tijeras. ¡Perdiste!")
        else:
            print("Las tijeras cortan el papel. ¡Ganaste!")

def main():
    # Crear una instancia de la clase IA
    ia = IA()

    while True:
        # Obtener la elección del jugador humano por teclado
        accion_usuario = input("\nElige una opción: piedra, papel o tijeras (q para salir): ")

        # Salir del bucle si el jugador decide salir
        if accion_usuario.lower() == 'q':
            break

        # Obtener la elección de la IA
        accion_computadora = ia.obtener_accion_ia()

        # Evaluar el resultado del juego
        evaluar_juego(accion_usuario, accion_computadora, ia)

if __name__ == "__main__":
    main()
