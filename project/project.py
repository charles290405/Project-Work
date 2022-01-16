from random import randint 

class SnakesandLadders:
    SNAKES = {
        27: 8,
        34: 7,
        29: 3,
        69: 31,
        72: 36,
        77: 46,
        80: 41,
        96: 48,
        98: 49,
    }
    LADDERS = {
        4: 16,
        6: 25,
        12: 49,
        20: 40,
        38: 88,
        58: 62,
        71: 93,
        78: 84,
        86: 95,
    }
    
    LAST_TILE = 100
    
    def __init__(self, n_players, verbose = False):
        self.n_players = n_players
        self.verbose = verbose
        self.players = [0] * n_players
        self.turn = 0
        self.winner = None # can use to determine if