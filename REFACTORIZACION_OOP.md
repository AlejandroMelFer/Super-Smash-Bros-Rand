# Refactorización a Programación Orientada a Objetos

## Resumen

Se ha refactorizado el código del proyecto para usar **Programación Orientada a Objetos (POO)** en lugar de diccionarios. El código antiguo sigue funcionando, pero ahora tienes una versión mejorada con clases.

## Archivos Nuevos

### Módulos del Modelo

1. **`src/models.py`** - Clases principales del juego:
   - `Move`: Representa un movimiento con nombre, daño, tipo e intensidad
   - `Character`: Representa un personaje con sus estadísticas y movimientos
   - `Player`: Representa un jugador en combate con su personaje, vidas y porcentaje

2. **`src/data_loader.py`** - Carga los datos JSON:
   - `DataLoader`: Carga los JSON y los convierte en objetos
   - Crea personajes con todos sus movimientos
   - Proporciona métodos para crear jugadores

3. **`src/game_logic.py`** - Lógica del juego refactorizada:
   - `preguntarLuchador()`: Selección de personajes (ahora retorna objetos Player)
   - `quien_pega()`: Determina quién ataca
   - `ejecutar_turno()`: Ejecuta un turno completo de combate

4. **`src/narration.py`** - Sistema de narración:
   - `Narrator`: Clase que genera narraciones de combate
   - Métodos para describir ataques y daño
   - Genera el estado de los jugadores

5. **`src/main_oop.py`** - Nuevo punto de entrada:
   - Implementación completa del bucle de combate
   - Usa todas las clases nuevas
   - ¡Ahora el combate funciona de principio a fin!

## Cómo Ejecutar la Versión Nueva

```bash
python Super-Smash-Bros-Rand/src/main_oop.py
```

## Ventajas de la Versión OOP

### 1. **Encapsulación**
Antes:
```python
jugador = {
    "Vidas": 3,
    "Porcentaje": 0,
    "Nombre": "mario",
    # ... más datos
}
# Acceso directo: jugador["Porcentaje"] += daño
```

Ahora:
```python
jugador = Player(personaje, 1)
# Método claro: jugador.recibir_daño(daño)
```

### 2. **Código Más Claro**
Antes:
```python
def seMuere(personaje):
    if porcentaje >= kp:  # Variables indefinidas!
        # ... lógica complicada
```

Ahora:
```python
class Player:
    def calcular_probabilidad_ko(self) -> float:
        if self.porcentaje < self.ko_percent:
            return 0.0
        # ... lógica clara
```

### 3. **Type Hints**
Las clases tienen type hints que ayudan a detectar errores:
```python
def ejecutar_turno(atacante: Player, defensor: Player) -> dict:
    # El IDE sabe qué tipo de datos espera
```

### 4. **Reutilización**
Los JSON se cargan **una sola vez** al inicio (esto soluciona el TODO de percents.py:38):
```python
data_loader = DataLoader()  # Carga todo una vez
p1 = data_loader.crear_jugador('mario', 1)  # No recarga archivos
```

### 5. **Métodos Cohesivos**
Cada clase tiene sus responsabilidades:
- `Player`: Gestiona vidas, daño, ataques
- `Character`: Almacena datos del personaje
- `Narrator`: Genera narraciones
- `DataLoader`: Carga datos

## Comparación de Estructura

### Antes (Diccionarios)
```
main.py
  ├─ Carga JSON directamente
  ├─ Llama a percents.preguntarLuchador()
  │   └─ Retorna diccionario con datos mezclados
  └─ Bucle de combate comentado (no funciona)

percents.py
  ├─ cuantoDañoHace() - Abre JSON cada vez ❌
  └─ seMuere() - Variables indefinidas ❌

comments.py
  └─ narrar() - Función incompleta
```

### Ahora (OOP)
```
main_oop.py
  ├─ DataLoader (carga JSON una vez) ✓
  ├─ game_logic.preguntarLuchador() → Player object ✓
  └─ Bucle de combate completo ✓

models.py
  ├─ Move ✓
  ├─ Character ✓
  └─ Player
      ├─ recibir_daño() ✓
      ├─ calcular_probabilidad_ko() ✓
      └─ intentar_ko() ✓

narration.py
  └─ Narrator
      ├─ describir_ataque() ✓
      ├─ describir_daño() ✓
      └─ narrar_turno() ✓
```

## Ejemplo de Uso

```python
from data_loader import DataLoader
from game_logic import ejecutar_turno, quien_pega
from narration import Narrator

# Cargar datos
dl = DataLoader()
narrador = Narrator(dl.obtener_comentarios())

# Crear jugadores
p1 = dl.crear_jugador('mario', 1)
p2 = dl.crear_jugador('luigi', 2)

# Simular un turno
atacante, defensor = quien_pega(p1, p2)
resultado = ejecutar_turno(atacante, defensor)
print(narrador.narrar_turno(resultado))

# Ejemplo de salida:
# "Mario lanza un golpe certero hacia el enemigo Luigi se tambalea ligeramente por el golpe."
```

## Archivos Originales

Los archivos originales **NO han sido modificados**:
- `main.py` - Original intacto
- `percents.py` - Original intacto
- `comments.py` - Original intacto

Puedes seguir usando el código antiguo si lo necesitas, o migrar gradualmente a la versión OOP.

## Próximos Pasos Sugeridos

1. **Probar el juego completo**: Ejecuta `main_oop.py` y juega varias partidas
2. **Agregar características**:
   - Sistema de combos
   - Diferentes modos de juego
   - Guardado de estadísticas
3. **Mejorar la narración**: Agregar más variedad de descripciones
4. **Tests unitarios**: Crear pruebas para cada clase
5. **Migrar completamente**: Si te gusta la versión OOP, puedes reemplazar `main.py` con `main_oop.py`

## Notas Técnicas

- **Python 3.10+** requerido (por el uso de `tuple[Player, Player]`)
- Todos los type hints están incluidos
- La lógica de probabilidad de KO es idéntica a la original
- Los JSON no han cambiado, solo cómo se procesan
