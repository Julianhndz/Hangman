import os
import random
import time

def read():
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        data = [line.strip("\n") for line in f] # Convierte el archivo en una lista
    
    dict_data = {key: value for key, value in enumerate(data)} # Convierte la lista en un diccionario. Con la funcion "enumerate" enumera cada palabra de la lista, siendo cada número la llave y la palabra el valor
    return dict_data

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
        ) 
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper()) # Esta función reemplaza las vocales que esten con acento por una sin acento, adicional, con la funcion upper las cambia a ser mayusculas
    return s
    

def run():
    while True:
        try:
            vidas = 7
            v_symbol= vidas * "♥"
            dict_word = read() # Traemos la funcion read() que devuelve un diccionario con las palabras con las que se va a jugar y las guardamos en una variable
            game_word = normalize(dict_word.get(random.randint(1, len(dict_word) + 1))) # Se selecciona la palabra al azar(randint) dentro de las palabras del diccionario con la función get. Luego, con la funcion normalize creada anteriormente se itera por los caracteres de la palabra seleccionada y esta los reemplaza si encuentra alguno con tildes.
            r_word = len(game_word)* "_" # Se reemplazan las letras de la palabra por lineas. Se hace multiplicando su longitud con la función len() y "_"
            print("""
            .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
            | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
            | |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
            | | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
            | |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
            | |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
            | |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
            | | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
            | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
            | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
            '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
            ¡Bienvenido al Juego del Ahorcado!
            -- Debes completar el juego antes de perder las 7 vidas que tienes --
                            -- Adivina la siguiente palabra --

            """)
            print(f"Vidas: {v_symbol}")

            while game_word != r_word:
                print(r_word.upper())
                l = normalize(input("-- Intenta una letra: "))
                if len(l) != 1 or int(l.isnumeric()):
                    raise ValueError
                elif l in game_word:
                    r_word = list(r_word)
                    for i, x in enumerate(game_word):
                        if x == l:
                            r_word[i] = x
                    r_word = "".join(r_word)
                else:
                    print("La letra que ingresaste no es de la palabra")
                    vidas -= 1
                    v_symbol = vidas * "♥"
                    print(f"Vidas restantes: {v_symbol}")
                    if vidas == 0:
                        print(f"Te has quedado sin vidas. La palabra era {game_word}")
                        break
                time.sleep(1)
                os.system("cls")
            print(f"¡Felicitaciones! Tu palabra era: {r_word}")

            play_again = int(input("""¿Quieres jugar de nuevo?
            SI: Oprime 1
            No: Oprime 2
            """))
            if play_again == 1:
                os.system("cls")
                run()
            else:
                print("¡Gracias por jugar!")
                break
        except ValueError:
            print("Solamente debes ingresar una letra. Tampoco se aceptan números")
            break


if __name__ == "__main__":
    run()