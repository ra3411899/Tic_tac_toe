from shutil import move


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3 x 3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j * 3, (j + 1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
        
    def available_move(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        # return len(self.available_move())
        return self.board.count(' ')

def play(game, s_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter
    # itearate while game still has empty squares
    # we dont have to worry about winner because we'll just return that
    # which breaks the loop
    while game.empty_squares():
        pass


# obj = TicTacToe()
# obj.print_board()
# obj.print_board_nums()
# obj.available_move()
# obj.print_board()