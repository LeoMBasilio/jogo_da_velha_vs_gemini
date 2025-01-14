from Controllers import Multplayer, Multplayer_Ai
from asyncio import sleep

while True:
    print(fr'''  
     ___                         _         _   _      _ _           
    |_  |                       | |       | | | |    | | |          
      | | ___   __ _  ___     __| | __ _  | | | | ___| | |__   __ _ 
      | |/ _ \ / _` |/ _ \   / _` |/ _` | | | | |/ _ \ | '_ \ / _` |
  /\__/ / (_) | (_| | (_) | | (_| | (_| | \ \_/ /  __/ | | | | (_| |
  \____/ \___/ \__, |\___/   \__,_|\__,_|  \___/ \___|_|_| |_|\__,_|
                __/ |                                               
               |___/                                                ''')

    print("Welcome to ")
    print("1. Multiplayer")
    print("2. Multiplayer AI")
    print("0. Exit")
    while True:
        try:
            match int(input()):
                case 1:
                    Multplayer.multPlayer()
                    break
                case 2:
                    Multplayer_Ai.multplayer_Ai()
                    break
                case 0:
                    exit()
                case _:
                    print("Invalid option")
                    continue
        except ValueError:
            print("Invalid option")
            continue
    
    print("Do you want to play again?")
    print("1. Yes")
    print("0. No")
    while True:
        try:
            match int(input()):
                case 1:
                    break
                case 0:
                    exit()
                case _:
                    print("Invalid option")
                    continue
        except ValueError:
            print("Invalid option")
            continue