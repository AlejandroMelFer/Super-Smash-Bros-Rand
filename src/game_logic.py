"""
Lógica del juego refactorizada usando clases
"""
import random
from models import Player
from data_loader import DataLoader


def preguntarLuchador(data_loader: DataLoader, num: int) -> Player:
    """
    Solicita al usuario que seleccione un personaje y crea un jugador

    Args:
        data_loader: Instancia de DataLoader con los datos cargados
        num: Número del jugador (1 o 2)

    Returns:
        Player: Objeto jugador con el personaje seleccionado
    """
    personajes = data_loader.listar_personajes()

    while True:
        c = input(f"Escribe el nombre del jugador {num}: ").lower()
        if c in personajes:
            return data_loader.crear_jugador(c, num)
        print("Escribe bien el nombre gilipollas, dale a enter y ponlo bien anda")
        input("")


def quien_pega(p1: Player, p2: Player) -> tuple[Player, Player]:
    """
    Determina aleatoriamente quién ataca y quién defiende

    Args:
        p1: Jugador 1
        p2: Jugador 2

    Returns:
        tuple: (atacante, defensor)
    """
    if random.randint(1, 2) == 1:
        return p1, p2
    else:
        return p2, p1


def ejecutar_turno(atacante: Player, defensor: Player) -> dict:
    """
    Ejecuta un turno de combate

    Args:
        atacante: Jugador que ataca
        defensor: Jugador que defiende

    Returns:
        dict: Información del turno (movimiento, daño, ko)
    """
    # El atacante realiza un ataque
    movimiento = atacante.atacar()

    # El defensor recibe el daño
    defensor.recibir_daño(movimiento.daño)

    # Verificar si hay KO
    ko = False
    if defensor.intentar_ko():
        defensor.perder_vida()
        ko = True

    return {
        "atacante": atacante,
        "defensor": defensor,
        "movimiento": movimiento,
        "daño": movimiento.daño,
        "ko": ko,
        "porcentaje_final": defensor.porcentaje
    }
