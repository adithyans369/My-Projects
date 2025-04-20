import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = np.zeros(9, dtype=int)
        self.current_player = 1
        self.done = False
        self.winner = None
        return self.board.copy()

    def available_actions(self):
        return [i for i in range(9) if self.board[i] == 0]

    def make_move(self, action, player=None):
        if self.done or self.board[action] != 0:
            return False
        if player is not None:
            self.current_player = player
        self.board[action] = self.current_player
        self.check_done()
        self.current_player *= -1
        return True

    def check_done(self):
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            col = self.board[i::3]
            if abs(sum(row)) == 3:
                self.done = True
                self.winner = np.sign(sum(row))
            if abs(sum(col)) == 3:
                self.done = True
                self.winner = np.sign(sum(col))
        diag1 = self.board[0] + self.board[4] + self.board[8]
        diag2 = self.board[2] + self.board[4] + self.board[6]
        if abs(diag1) == 3 or abs(diag2) == 3:
            self.done = True
            self.winner = np.sign(diag1 if abs(diag1) == 3 else diag2)
        if not self.done and 0 not in self.board:
            self.done = True
            self.winner = 0

    def get_state(self):
        return self.board.copy()
