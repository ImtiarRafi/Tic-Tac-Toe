from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # a list of nine length as the board is 3*3 board.
        self.current_winner = None  # created to check for current winners when the game is running

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:  # to traverse the board from 0-3, 3-6, 6-9
            print(' | ' + ' | '.join(row) + ' | ')  # vertical lines are separators of the rows, rows are joined

    @staticmethod
    def print_board_nums():  # #0,1,2 |5 etc numbers to position marking
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']  # returns a list of empty spaces in the board

    def empty_squares(self):
        return ' ' in self.board  # check for empty spaces in the board

    def num_empty_squares(self):
        return self.board.count(' ')  # counts number of empty square spaces

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check rows
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # check columns
        col_index = square % 3
        col = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals
        if square % 2 == 0:
            dia1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in dia1]):
                return True

            dia2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in dia2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X' #switching letters

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
