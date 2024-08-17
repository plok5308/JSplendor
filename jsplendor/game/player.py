from jsplendor.game.abs import GameComponent

class Player(GameComponent):
    def __init__(self, development_cards, noble_cards, coins):
        super().__init__(development_cards, noble_cards, coins)

    def print_status(self, object_name=None):
        if object_name is not None:
            print("[{}]".format(object_name))

        print("The number of development cards: {}".format(len(self.development_cards)))
        print("Noble cards: ")
        print(self.noble_cards)
        print("Coin status: ")
        print(self.coins)    
        print("")