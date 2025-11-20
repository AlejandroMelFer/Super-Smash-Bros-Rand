import main
import json
import os
from pathlib import Path
import random
import comments
import percents

def comentarios(c1,c2):
    golpeador = percents.quienPega(c1,c2)
    golpeado = c1 if golpeador == c2 else c2
    print("")