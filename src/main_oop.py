"""
Punto de entrada principal del juego - Versión orientada a objetos
"""
import os
import time
from data_loader import DataLoader
from game_logic import preguntarLuchador, quien_pega, ejecutar_turno
from narration import Narrator


def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """Función principal del juego"""
    # Cargar datos
    data_loader = DataLoader()
    narrador = Narrator(data_loader.obtener_comentarios())

    # Limpiar pantalla inicial
    limpiar_pantalla()

    # Presentación
    print("=" * 80)
    print("Bienvenido a Super Smash Bros Rand")
    print("El simulador de peleas de la version Super Smash Bros Melee")
    print("con sus personajes iniciales.")
    print("=" * 80)
    print()

    # Mostrar personajes disponibles
    print("Personajes jugables:")
    personajes = data_loader.listar_personajes()
    for i, p in enumerate(personajes, 1):
        print(f"{i}. {p.capitalize()}")
    print()

    # Selección de jugadores
    j1 = preguntarLuchador(data_loader, 1)
    j2 = preguntarLuchador(data_loader, 2)

    # Cuenta regresiva
    print("\n¡QUE EMPIECE EL COMBATE EN:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1.5)

    limpiar_pantalla()

    # Bucle principal del combate
    turno = 0
    while j1.esta_vivo() and j2.esta_vivo():
        turno += 1

        print(f"\n{'='*80}")
        print(f"TURNO {turno}")
        print(f"{'='*80}")
        print()

        # Mostrar estado actual
        print(narrador.mostrar_estado(j1, j2))
        print()

        # Determinar quién ataca
        atacante, defensor = quien_pega(j1, j2)

        # Ejecutar turno
        resultado = ejecutar_turno(atacante, defensor)

        # Narrar el turno
        narracion = narrador.narrar_turno(resultado)
        print(narracion)
        print()

        # Pausa para que el jugador pueda leer
        input("Presiona ENTER para continuar...")
        limpiar_pantalla()

    # Fin del combate
    print("\n" + "=" * 80)
    print("¡FIN DEL COMBATE!")
    print("=" * 80)
    print()

    # Determinar ganador
    if j1.esta_vivo():
        ganador = j1
        perdedor = j2
    else:
        ganador = j2
        perdedor = j1

    print(f"🏆 ¡{ganador.nombre.upper()} ES EL GANADOR! 🏆")
    print()
    print(f"{ganador.nombre.capitalize()}: {ganador.vidas} {'vida' if ganador.vidas == 1 else 'vidas'} restante{'s' if ganador.vidas != 1 else ''} | {ganador.porcentaje:.1f}%")
    print(f"{perdedor.nombre.capitalize()}: Eliminado")
    print()


if __name__ == "__main__":
    main()
