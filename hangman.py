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
            print(f"Vidas: {v_symbol}") # Imprime las vidas con simbolo de corazon

            while game_word != r_word: # Ciclo que se repite hasta que la condición sea diferente. En este caso, el while se repite siempre y cuando la palabra la cual se esta jugando "r_word" sea diferente a la que se debe adivinar "game_word".
                print(r_word.upper())
                l = normalize(input("-- Intenta una letra: ")) # Input que permite al usuario ingresar la letra para jugar
                if len(l) != 1 or int(l.isnumeric()): # Esta if sentence limita la cantidad de letras a ingresar a solamente una, asi como tambien valida que el caracter ingresado sea una letra y no un numero.
                    raise ValueError # En caso de que se cumpla la condición se levanta una excepción de ValueError, esto para poder manejarlo mas adelante.
                elif l in game_word: # Valida si la letra ingresada esta dentro de la palabra que se esta jugando, si esta, entra la logica del codigo.
                    r_word = list(r_word) # Se convierte la palabra de juego en una lista
                    for i, x in enumerate(game_word): # Enumera los puestos de cada caracter en la palabra comenzando desde el 0. Al ser un diccionario se pasan dos parametros i, x los cuales serian respectivamente key y value del diccionario
                        if x == l: # Se compara si la letra ingresada "l" es igual a "x" dentro de la palabra.
                            r_word[i] = x # Se asigna la letra "x" en la posicion "i" a la que pertence.
                    r_word = "".join(r_word) # Se usa la función "".join() para unir los caracteres nuevamente en una palabra completa
                else: # Este else valida que la letra que se ingreso no esta en la palabra y tambien maneja el reducir de las vidas de juego que se tiene implementado
                    print("La letra que ingresaste no es de la palabra")
                    vidas -= 1
                    v_symbol = vidas * "♥"
                    print(f"Vidas restantes: {v_symbol}")
                    if vidas == 0: # if sentence que valida y se activa unicamente si las vidas llegan a 0.
                        print(f"Te has quedado sin vidas. La palabra era {game_word}")
                        break
                time.sleep(1)
                os.system("cls")
            print(f"¡Felicitaciones! Tu palabra era: {r_word.upper}") # Se imprime la palabra en consola cuando se logran adivinar todas las letras que la componen dentro de los 7 intentos predeterminados

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
        except ValueError: # Se le da manejo a la excepción del ValueError que se invoco mas arriba en la misma función; esto para evitar errores al momento de la ejecución del proprama            print("Solamente debes ingresar una letra. Tampoco se aceptan números")
            break


if __name__ == "__main__":
    run()