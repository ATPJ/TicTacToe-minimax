class TicTacToe:
    def __init__(self, pruning: bool) -> None:
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.player = "X"
        self.counter = 0
        self.pruning = pruning

    def show_board(self):
        print()
        for i, r in enumerate(self.board):
            for j, c in enumerate(r):
                if j == 2:
                    print("   ") if c == '.' else print(f" {c} ")
                else:
                    print("   ", end=" | ") if c == '.' else print(f" {c} ", end=" | ")
            if i != 2:
                print("----------------")
            else:
                print()

    def is_end(self) -> tuple[bool, str | None]:
        # check vertical
        for j in range(3):
            if (self.board[0][j] != '.' and
                self.board[0][j] == self.board[1][j] and
                self.board[1][j] == self.board[2][j]):

                return (True, self.board[0][j])

        # check horizantal
        for i in range(3):
            if (self.board[i][0] != '.' and
                self.board[i][0] == self.board[i][1] and
                self.board[i][1] == self.board[i][2]):
                return (True, self.board[i][0])

        # check diagonal
        if (self.board[0][0] != '.' and
            self.board[0][0] == self.board[1][1] and
            self.board[1][1] == self.board[2][2]):
            return (True, self.board[0][0])

        if (self.board[0][2] != '.' and
            self.board[0][2] == self.board[1][1] and
            self.board[1][1] == self.board[2][0]):
            return (True, self.board[0][2])

        # check if the board is full.
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != '.':
                    count += 1
        if count == 9:
            return (True, None)

        return (False, None)

    def is_valid_move(self, i, j):
        if self.board[i][j] != '.':
            return False
        if i < 0 or i > 2 or j < 0 or j > 2:
            return False
        return True

    def minimax_alpha_beta(self,
                           depth,
                           is_max: bool,
                           alpha=-10000,
                           beta=10000):
        self.counter += 1
        is_end, winner = self.is_end()
        if is_end:
            if winner == self.player:
                return 10 - depth
            elif winner is not None:
                return -10 + depth
            else:
                return 0

        best = -1000 if is_max else 1000

        if is_max:
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.board[i][j] = self.player
                        value = self.minimax_alpha_beta(depth+1,
                                                        False,
                                                        alpha,
                                                        beta)
                        self.board[i][j] = "."
                        if (value > best):
                            best = value
                            alpha = max(value, alpha)

                        if self.pruning:
                            if alpha >= beta:
                                break
        else:
            for i in range(3):
                for j in range(3):
                    if self.is_valid_move(i, j):
                        self.board[i][j] = "X" if self.player == "O" else "O"
                        value = self.minimax_alpha_beta(depth+1,
                                                        True,
                                                        alpha,
                                                        beta)
                        self.board[i][j] = "."
                        if (value < best):
                            best = value
                            beta = min(value, beta)

                        if self.pruning:
                            if alpha >= beta:
                                break

        return best

    def find_best_move(self):
        best_val = -1000
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):

                if self.is_valid_move(i, j):
                    self.board[i][j] = self.player
                    move_value = self.minimax_alpha_beta(0, False)
                    self.board[i][j] = "."

                    if (move_value > best_val):
                        best_val = move_value
                        best_move = (i, j)

        return (best_val, best_move)

    def move(self, i, j) -> True:
        if not self.is_valid_move(i, j):
            raise Exception("Invalid move.")

        self.board[i][j] = self.player
        self.player = "X" if self.player == "O" else "O"

        is_end, winner = self.is_end()
        if is_end:
            if winner:
                print(f"The winner is {winner}.")
                return True
            else:
                print("DRAW!")
                return True

        return False
