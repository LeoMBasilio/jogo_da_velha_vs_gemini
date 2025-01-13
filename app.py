from Controllers import Multplayer, Multplayer_Ai
from asyncio import sleep

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
                Multplayer_Ai.multplayer_AI()
                break
            case 0:
                exit()
            case _:
                print("Invalid option")
                continue
    except ValueError:
        print("Invalid option")
        continue