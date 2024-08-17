from jsplendor.game.abs import GameComponent

class Board(GameComponent):
    def __init__(self, development_cards, noble_cards, coins):
        super().__init__(development_cards, noble_cards, coins)
        self._split_development_cards()

    def _split_development_cards(self):
        self.level1_cards = []
        self.level2_cards = []
        self.level3_cards = []

        for card in self.development_cards:
            if card.level==1:
                self.level1_cards.append(card)
            elif card.level==2:
                self.level2_cards.append(card)
            elif card.level==3:
                self.level3_cards.append(card)
            else:
                raise ValueError
            
    def print_status(self, object_name=None):
        if object_name is not None:
            print("[{}]".format(object_name))
            
        print("The number of level1 development cards: {}".format(len(self.level1_cards)))
        print("The number of level2 development cards: {}".format(len(self.level2_cards)))
        print("The number of level3 development cards: {}".format(len(self.level3_cards)))
        print("Noble cards: ")
        for noble_card in self.noble_cards:
            noble_card.print()
        print("Coin status: ")
        print(self.coins())    
        print("")

