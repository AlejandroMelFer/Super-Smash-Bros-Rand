"""
Script de prueba para verificar la refactorización OOP
"""
from data_loader import DataLoader
from game_logic import quien_pega, ejecutar_turno
from narration import Narrator


def prueba_carga_datos():
    """Prueba que los datos se cargan correctamente"""
    print("=" * 60)
    print("PRUEBA 1: Carga de Datos")
    print("=" * 60)

    dl = DataLoader()
    print(f"✓ {len(dl.personajes)} personajes cargados")
    print(f"✓ Personajes disponibles: {', '.join(dl.listar_personajes())}")
    print()
    return dl


def prueba_personajes(dl):
    """Prueba la creación de personajes"""
    print("=" * 60)
    print("PRUEBA 2: Personajes y Movimientos")
    print("=" * 60)

    mario = dl.obtener_personaje('mario')
    print(f"✓ Personaje cargado: {mario}")
    print(f"✓ KO percent: {mario.ko_percent}%")
    print(f"✓ Número de movimientos: {len(mario.movimientos)}")
    print(f"✓ Ejemplos de movimientos:")
    for mov in mario.movimientos[:3]:
        print(f"  - {mov.nombre}: {mov.daño} dmg ({mov.tipo}, {mov.intensidad})")
    print()


def prueba_jugadores(dl):
    """Prueba la creación de jugadores"""
    print("=" * 60)
    print("PRUEBA 3: Jugadores y Combate")
    print("=" * 60)

    p1 = dl.crear_jugador('mario', 1)
    p2 = dl.crear_jugador('fox', 2)

    print(f"✓ Jugador 1: {p1}")
    print(f"✓ Jugador 2: {p2}")
    print()

    # Simular daño
    print("Simulando combate:")
    p1.recibir_daño(50)
    print(f"  Mario recibe 50 de daño: {p1}")

    p1.recibir_daño(60)
    prob = p1.calcular_probabilidad_ko()
    print(f"  Mario recibe 60 más de daño: {p1}")
    print(f"  Probabilidad de KO: {prob:.0%}")
    print()

    return p1, p2


def prueba_turnos(dl):
    """Prueba la ejecución de turnos"""
    print("=" * 60)
    print("PRUEBA 4: Turnos y Narración")
    print("=" * 60)

    p1 = dl.crear_jugador('luigi', 1)
    p2 = dl.crear_jugador('pikachu', 2)
    narrador = Narrator(dl.obtener_comentarios())

    print("Estado inicial:")
    print(narrador.mostrar_estado(p1, p2))
    print()

    print("Simulando 3 turnos:")
    for i in range(1, 4):
        print(f"\nTurno {i}:")
        atacante, defensor = quien_pega(p1, p2)
        resultado = ejecutar_turno(atacante, defensor)
        print(narrador.narrar_turno(resultado))

    print("\nEstado final:")
    print(narrador.mostrar_estado(p1, p2))
    print()


def prueba_ko(dl):
    """Prueba el sistema de KO"""
    print("=" * 60)
    print("PRUEBA 5: Sistema de KO")
    print("=" * 60)

    p = dl.crear_jugador('kirby', 1)
    narrador = Narrator(dl.obtener_comentarios())

    print(f"Personaje: {p.nombre} (KO% = {p.ko_percent})")
    print(f"Vidas iniciales: {p.vidas}")
    print()

    # Aplicar daño hasta pasar el KO percent
    p.recibir_daño(120)
    print(f"Después de recibir 120 de daño: {p}")
    print(f"Probabilidad de KO: {p.calcular_probabilidad_ko():.0%}")

    # Intentar KO
    if p.intentar_ko():
        print("✓ ¡KO exitoso!")
        print(f"  Vidas restantes: {p.vidas}")
        print(f"  Porcentaje reseteado: {p.porcentaje}%")
    else:
        print("✗ El jugador sobrevivió")
    print()


def main():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "PRUEBAS DE REFACTORIZACIÓN OOP" + " " * 18 + "║")
    print("╚" + "═" * 58 + "╝")
    print()

    try:
        dl = prueba_carga_datos()
        prueba_personajes(dl)
        prueba_jugadores(dl)
        prueba_turnos(dl)
        prueba_ko(dl)

        print("=" * 60)
        print("✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 60)
        print()
        print("El código OOP está funcionando correctamente.")
        print("Puedes ejecutar 'python main_oop.py' para jugar.")
        print()

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
