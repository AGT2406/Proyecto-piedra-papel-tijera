import pytest
from piedra_papel_tijera import IA, evaluar_juego

# Prueba para verificar que el resultado es empate cuando ambas acciones son iguales
def test_empate():
    ia = IA()
    accion_computadora = ia.obtener_accion_ia()
    resultado = evaluar_juego(accion_computadora, accion_computadora)
    assert resultado == f"Ambos eligieron {accion_computadora}. ¡Empate!"

# Prueba para verificar que el resultado es victoria para el jugador cuando la IA elige una acción que pierde
def test_victoria_jugador():
    ia = IA()
    resultado = evaluar_juego("piedra", "tijeras")
    assert resultado == "La piedra aplasta las tijeras. ¡Ganaste!"

# Prueba para verificar que el resultado es derrota para el jugador cuando la IA elige una acción que gana
def test_derrota_jugador():
    ia = IA()
    resultado = evaluar_juego("tijeras", "papel")
    assert resultado == "Las tijeras cortan el papel. ¡Perdiste!"

# Prueba para verificar que el resultado es victoria para el jugador cuando la IA elige "lagarto" si el jugador escogió "piedra"
def test_victoria_ia_lagarto():
    ia = IA()
    resultado = evaluar_juego("piedra", "lagarto")
    assert resultado == "La piedra aplasta el lagarto. ¡Ganaste!"

# Prueba para verificar que el resultado es victoria para el jugador cuando la IA elige "spock" si el jugador escogió "tijeras"
def test_victoria_ia_spock():
    ia = IA()
    resultado = evaluar_juego("tijeras", "spock")
    assert resultado == "Spock aplasta las tijeras. ¡Ganaste!"
