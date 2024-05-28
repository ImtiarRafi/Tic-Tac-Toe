import math
import random


class Player:
    def __init__(self, letter):
        # letter x or o these are represented by the player
        self.letter = letter

    def get_move(self, game):  # for players to get their next move
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())  # get a valid random spot for next move
        return square


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9) : ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try Again')
        return val
class GeniusComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #random choosing at the starting
        else:
            square = self.minimax(game,self.letter)['position'] #positionwise play with minimax implementing for most optimal move
        return square

    def minimax(self,state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score':1 * (state.num_empty_squares()+1) if other_player == max_player else
                    -1 * (state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():
            return {'position' : None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  #each score should be maximized,

            '''This is because the maximizing player aims to find the highest possible score, 
            and starting from negative infinity ensures that any score found will be higher.'''

        else:
            best = {'position': None, 'score': math.inf} # each score should be minimized

            ''' This is because the minimizing player aims to find the lowest possible score, 
            and starting from positive infinity ensures that any score found will be lower.'''

        for possible_move in state.available_moves():
            #step 1 : make a move, try that spot
            state.make_move(possible_move,player)

            #step 2: recurse using minimax to simulate a game after making that move

            sim_score = self.minimax(state,other_player) #after playing our move we alternate to other player

            #step 3 : undo the move so that we can try another move

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #simulated score will be generated playing in possible move and if this is not done  recursion wont work properly.

            #step 4 : update dict if needed

            if player == max_player: # tryin to maximize the max_player
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else: # tryin to minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score

        return  best
