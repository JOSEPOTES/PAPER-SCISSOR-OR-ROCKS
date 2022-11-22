import random
from termcolor import colored
def operation(user_name):
    empate = 0
    victorias = 0
    derrotas = 0
    print(f" {user_name.capitalize()} Escribe cuando quieras " +  colored('salir','yellow',attrs=['bold']) + " y terminamos el juego ")
    pasar = input(" Presiona " + colored('ENTER',"green",attrs=['bold']) + " para continuar: ")
    while True:
        options = ["Piedra","Papel","Tijera"]
        user_choose = input("Escribe una opcion: ").capitalize()
        random_option = random.choice(options)
        machine_think = []
        saving_option = machine_think.append(random_option)
        string_word = " ".join(machine_think).capitalize()
        if not user_choose in options:
            print("Opcion no valida.")
            continue
        elif string_word == user_choose:
            print(f"Empatamos en {string_word}")
            empate += 1
            print(f"Tenemos {empate} en este juego")
        elif string_word == 'Tijera' and user_choose == 'Papel':
            print(f"Maquina gana")
            derrotas += 1
            print(f"Haz perdido {derrotas} en este juego")
        elif string_word == "Piedra" and user_choose == "Tijera":
            print(f"Maquina gana")
            derrotas += 1
            print(f" Haz perdido {derrotas}")
        elif string_word == "Papel" and user_choose == "Piedra":
            print(f" Maquina gana")
            derrotas += 1
            print(f"Haz perdido {derrotas}")
        else:
            print(f"Haz ganado con {user_choose} y yo he elegido {string_word}")
            victorias += 1
            print(f"Haz ganado {victorias} en este juego")
            salir = input(" Escribe " + colored('salir','yellow',attrs=["bold"]) + " y terminamos el juego: ").lower()
            if salir == "salir":
                break
            else:
                continue
def run():
    user_name = input("Escribe tu nombre: ")
    print(f"Hola {user_name.capitalize()}, que valiente eres!, quieres jugar contra mi!, veamos si puedes!.", "\n", "Vas a tener varias opciones")
    print("Piedra,Papel o Tijeras, deberas elegir una.")
    operation(user_name)
if __name__ == "__main__":
    run()