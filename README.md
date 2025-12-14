# Super-Smash-Bros-Rand
Smash random Game
Un juego de smash basado en aleatoriedad, escalable

## Configuración del Token de Discord

Para que el bot de Discord funcione correctamente, es necesario proporcionar un token de bot. Sigue estos pasos para configurarlo:

1.  **Crea el archivo de secretos**: Copia el archivo `src/SBRsecrets.py.example` a `src/SBRsecrets.py`.
2.  **Edita el archivo de secretos**: Abre `src/SBRsecrets.py` y reemplaza `"TOKEN DE DISCORD"` con tu token real de bot de Discord.

    ```python
    # src/SBRsecrets.py
    token = "TU_TOKEN_REAL_DE_DISCORD"
    ```

    **Importante**: No compartas tu `src/SBRsecrets.py` con nadie ni lo subas a un repositorio público, ya que contiene información sensible. El archivo `.gitignore` ya está configurado para ignorar `src/SBRsecrets.py`.