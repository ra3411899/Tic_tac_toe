import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter # letter is x or o
    
    #we want all player to get their next move given a game
    def get_move(self, game):
        pass
    

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.availabe_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None 
        while not valid_square:
            square = input(self.letter + '\'S turn. Input move (0-9):')
            # we re going to check that this is a correct value by trying to cast
            # it to an interget, and it it's not, then we say its invalid 
            # if that spot is not availabeon the baord we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                 print('Invalid Square, Try Again.')

        return val

