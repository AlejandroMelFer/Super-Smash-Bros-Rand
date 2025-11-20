import json
import os
from pathlib import Path
import time

def main():
    base = Path(__file__).resolve().parent
    ruta = base / ".." / "characters.json"
    os.system("cls")
    print("Bienvenido a Super Smash Bros Rand, el simulador de peleas de la version Super Smash Bros Melee con sus personajes inciales.")
    print("Personajes jugables:")
    with ruta.open("r",encoding="utf-8") as file:
        datos = json.load(file)
        personajes = list(datos["Characters"].keys())
        counter = 1
        for p in personajes:
            print(f"{counter}.{p.capitalize()}")
            counter+=1
        c1 = input("Escribe el nombre del luchador 1: ")
        if c1.lower() not in personajes:
            while True:
                print("Escribe el nombre bien, gilipollas, dale a enter y vuelve a intentarlo")
                input("")
                main()
        c2 = input("Escribe el nombre del luchador 2: ")
        if c2.lower() not in personajes:
            while True:
                print("Escribe el nombre bien, gilipollas, dale a enter y vuelve a intentarlo")
                input("")
                main()
        print("QUE EMPIECE LA BATALLA EN")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        os.system("cls")
        print("sxc")
        print("Hola")            
        print("hola")

if __name__ == "__main__":
    main()