from jsplendor.game.abs import GameComponent
from jsplendor.utils import Element

class Player(GameComponent):
    def __init__(self, name, development_cards, noble_cards, coins):
        super().__init__(name, development_cards, noble_cards, coins)

    def get_a_coin(self, board, color):
        if board.coins[color] > 0:
            board.coins[color] -= 1
            self.coins[color] += 1
            print('{} get a {} coin.'.format(self.name, color))
        else:
            pass

    def is_possible_to_buy(self, card):
        price = card.price
        is_possible = True
        for key, value in self.coins.items():
            if key=="GOLD":
                pass
            else: 
                if price[Element[key].value] > value:
                    is_possible = False
                    break

        return is_possible
    
    def buy_development_card(self, board, card_position):
        assert(card_position>=0 and card_position<=5)

        if card_position < 3:
            candidated_card = board.level1_cards[card_position]
        elif card_position < 6:
            candidated_card = board.level2_cards[card_position-3]

        if self.is_possible_to_buy(candidated_card):
            price = candidated_card.price
            for key in self.coins.keys():
                if key=="GOLD":
                    pass
                else:
                    self.coins[key] -= price[Element[key].value]

            self.development_cards.append(candidated_card)
            
            print('{} get a {} card.'.format(self.name, candidated_card))
        else:
            print('Not enough tokens.')

    def print_status(self, object_name=None):
        if object_name is not None:
            print("[{}]".format(object_name))

        print("Development cards: ")
        print(self.development_cards)
        print("Noble cards: ")
        print(self.noble_cards)
        print("Coin status: ")
        print(self.coins)    
        print("")

