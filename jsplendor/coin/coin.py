from jsplendor.utils import Element


class Coins:
    def __init__(self):
        self.coins = dict()
        for name in Element.__members__.keys():
            self.coins[name] = 0

    def __call__(self):
        return self.coins
    
    def set_full_coin_to_board(self):
        self.coins["WHITE"] = 4
        self.coins["BLUE"] = 4
        self.coins["GREEN"] = 4
        self.coins["RED"] = 4
        self.coins["BLACK"] = 4
        self.coins["GOLD"] = 5

def get_full_coin_for_board():
    coins = Coins()
    coins.set_full_coin_to_board()

    return coins

def get_empty_coin():
    coins = Coins()
    return coins
    
