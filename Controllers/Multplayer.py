from Models.Borad import Game
import os

def multPlayer():
    game = Game()
    while True:
        os.system("cls")
        board = game.get_board()
        for row in board:
            print(row)
        print()
        if game.check_winner():
            print(f"Player {game.check_winner()} wins!")
            break
        if game.check_draw():
            print("Draw!")
            break
        print(f"Player {game.get_turn()}'s turn")
        while True:
            match int(input()):
                case 1:
                    game.move(0, 0)
                    break
                case 2:
                    game.move(0, 1)
                    break
                case 3:
                    game.move(0, 2)
                    break
                case 4:
                    game.move(1, 0)
                    break
                case 5:
                    game.move(1, 1)
                    break
                case 6:
                    game.move(1, 2)
                    break
                case 7:
                    game.move(2, 0)
                    break
                case 8:
                    game.move(2, 1)
                    break
                case 9:
                    game.move(2, 2)
                    break
                case _:
                    print("Invalid move")
                    continue
