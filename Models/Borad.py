class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 1

    def move(self, x, y):
        if self.board[x][y] == ' ':
            self.board[x][y] = ' x ' if self.turn == 1 else ' o '
            self.turn = 2 if self.turn == 1 else 1

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return 0

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def get_board(self):
        return self.board

    def get_turn(self):
        return self.turn

    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 1
        