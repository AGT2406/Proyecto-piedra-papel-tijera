import random

# Definición de las opciones del juego
PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERAS = 'tijeras'
LAGARTO = 'lagarto'
SPOCK = 'spock'

class IA:
    def __init__(self):
        # Lista de opciones del juego
        self.acciones_juego = [PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK]
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
            elif jugada_mas_comun == LAGARTO:
                return SPOCK
            elif jugada_mas_comun == SPOCK:
                return TIJERAS

    def actualizar_jugadas_aprendidas(self, jugada):
        # Actualizar el diccionario de jugadas aprendidas
        if jugada in self.jugadas_aprendidas:
            self.jugadas_aprendidas[jugada] += 1
        else:
            self.jugadas_aprendidas[jugada] = 1

class Juego:
    def __init__(self):
        # Crear una instancia de la clase IA
        self.ia = IA()

    def evaluar_juego(self, accion_usuario):
        # Obtener la elección de la IA
        accion_computadora = self.ia.obtener_accion_ia()

        # Evaluar el resultado del juego
        print(f"\nTu elección: {accion_usuario}. La computadora eligió: {accion_computadora}")

        # Actualizar las jugadas aprendidas de la inteligencia artificial
        self.ia.actualizar_jugadas_aprendidas(accion_computadora)

        if accion_usuario == accion_computadora:
            print(f"Ambos eligieron {accion_usuario}. ¡Empate!")

        elif accion_usuario == PIEDRA:
            if accion_computadora in [TIJERAS, LAGARTO]:
                print(f"La piedra aplasta {accion_computadora}. ¡Ganaste!")
            else:
                print(f"{accion_computadora} desintegra la piedra. ¡Perdiste!")

        elif accion_usuario == PAPEL:
            if accion_computadora in [PIEDRA, SPOCK]:
                print(f"El papel envuelve {accion_computadora}. ¡Ganaste!")
            else:
                print(f"{accion_computadora} desaprueba el papel. ¡Perdiste!")

        elif accion_usuario == TIJERAS:
            if accion_computadora in [PAPEL, LAGARTO]:
                print(f"Las tijeras cortan {accion_computadora}. ¡Ganaste!")
            else:
                print(f"{accion_computadora} decapitan las tijeras. ¡Perdiste!")

        elif accion_usuario == LAGARTO:
            if accion_computadora in [PAPEL, SPOCK]:
                print(f"El lagarto devora {accion_computadora}. ¡Ganaste!")
            else:
                print(f"{accion_computadora} envenena al lagarto. ¡Perdiste!")

        elif accion_usuario == SPOCK:
            if accion_computadora in [PIEDRA, TIJERAS]:
                print(f"Spock aplasta {accion_computadora}. ¡Ganaste!")
            else:
                print(f"{accion_computadora} vaporiza a Spock. ¡Perdiste!")

def main():
    juego = Juego()

    while True:
        # Obtener la elección del jugador humano por teclado
        accion_usuario = input("\nElige una opción: piedra, papel, tijeras, lagarto o spock (q para salir): ")

        # Salir del bucle si el jugador decide salir
        if accion_usuario.lower() == 'q':
            break

        # Evaluar el resultado del juego
        juego.evaluar_juego(accion_usuario)

if __name__ == "__main__":
    main()
