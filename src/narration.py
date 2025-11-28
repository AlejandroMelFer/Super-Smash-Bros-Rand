"""
Sistema de narración de combate refactorizado usando clases
"""
import random
from models import Player, Move


class Narrator:
    """Genera narraciones de combate basadas en plantillas"""

    def __init__(self, comentarios: dict):
        """
        Inicializa el narrador con las plantillas de comentarios

        Args:
            comentarios: Diccionario con las plantillas cargadas de comments.json
        """
        self.comentarios = comentarios

    def describir_ataque(self, movimiento: Move) -> str:
        """
        Genera una descripción del ataque

        Args:
            movimiento: Movimiento realizado

        Returns:
            str: Descripción del ataque
        """
        tipo = movimiento.tipo
        intensidad = movimiento.intensidad

        # Manejar casos especiales
        if tipo == "reflector" or intensidad == "aturde":
            intensidad = "media"  # Usar plantillas medias para casos especiales

        plantillas = self.comentarios["ataque"].get(tipo, {}).get(intensidad, [])

        if not plantillas:
            return "ataca"

        descripcion = random.choice(plantillas)

        # Reemplazar placeholders si existen
        # TODO: Implementar reemplazo de {proyectil}, {golpe}, {hechizo} según el movimiento
        return descripcion

    def describir_daño(self, movimiento: Move) -> str:
        """
        Genera una descripción del daño recibido

        Args:
            movimiento: Movimiento que causó el daño

        Returns:
            str: Descripción del daño recibido
        """
        tipo = movimiento.tipo
        intensidad = movimiento.intensidad

        # Manejar casos especiales
        if tipo == "reflector":
            tipo = "fisico"
            intensidad = "media"
        elif tipo == "grapling":
            tipo = "grappling"  # Corregir el tipo para que coincida con comments.json

        if intensidad == "aturde":
            intensidad = "media"

        plantillas = self.comentarios["recibe"].get(tipo, {}).get(intensidad, [])

        if not plantillas:
            return "recibe el golpe"

        descripcion = random.choice(plantillas)

        # Reemplazar placeholders si existen
        return descripcion

    def narrar_turno(self, resultado_turno: dict) -> str:
        """
        Genera la narración completa de un turno

        Args:
            resultado_turno: Diccionario con información del turno

        Returns:
            str: Narración del turno
        """
        atacante = resultado_turno["atacante"]
        defensor = resultado_turno["defensor"]
        movimiento = resultado_turno["movimiento"]
        ko = resultado_turno["ko"]

        # Generar descripciones
        desc_ataque = self.describir_ataque(movimiento)
        desc_daño = self.describir_daño(movimiento)

        # Construir la narración
        narracion = f"{atacante.nombre.capitalize()} {desc_ataque} {defensor.nombre.capitalize()} {desc_daño}."

        # Agregar información de estado
        if ko:
            mensaje_ko = random.choice(self.comentarios["recibe"]["KO"])
            narracion += f"\n¡{defensor.nombre.capitalize()} {mensaje_ko}!"
        elif defensor.porcentaje >= defensor.ko_percent:
            mensaje_limite = random.choice(self.comentarios["recibe"]["limite"])
            narracion += f"\n{defensor.nombre.capitalize()} {mensaje_limite}."

        return narracion

    def mostrar_estado(self, p1: Player, p2: Player) -> str:
        """
        Genera un string con el estado actual de ambos jugadores

        Args:
            p1: Jugador 1
            p2: Jugador 2

        Returns:
            str: Estado formateado de ambos jugadores
        """
        lineas = []
        lineas.append(f"{p1.nombre.capitalize()}: {p1.porcentaje:.1f}% | {p1.vidas} {'vida' if p1.vidas == 1 else 'vidas'} restante{'s' if p1.vidas != 1 else ''}")
        lineas.append(f"{p2.nombre.capitalize()}: {p2.porcentaje:.1f}% | {p2.vidas} {'vida' if p2.vidas == 1 else 'vidas'} restante{'s' if p2.vidas != 1 else ''}")
        return "\n".join(lineas)
