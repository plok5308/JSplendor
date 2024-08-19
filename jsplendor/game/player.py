import numpy as np

from jsplendor.game.abs import GameComponent
from jsplendor.utils import Element
from jsplendor.game.utils import adjust_price, get_coin_comb


class Player(GameComponent):
    def __init__(self, name, development_cards, noble_cards, coins):
        super().__init__(name, development_cards, noble_cards, coins)
        self.n_coin_action = 10
        self.n_buy_action = 12
        self.num_actions = self.n_coin_action + self.n_buy_action
        self._update_score()

    def _update_score(self):
        sum_victory_point = 0
        sum_development_card_gem = np.zeros(5, dtype=int)
        for card in self.development_cards:
            sum_victory_point += card.victory_point
            gem_idx = Element[card.gem_color].value
            sum_development_card_gem[gem_idx] += 1

        for card in self.noble_cards:
            sum_victory_point += card.victory_point

        self.sum_victory_point = sum_victory_point
        self.sum_development_card_gem = sum_development_card_gem

    def do_action(self, board, action):
        if action < self.n_coin_action:
            self.get_coins(board, action)
        else:
            self.buy_development_card(board, action-self.n_coin_action)

        return self.sum_victory_point

    def get_all_possible_actions(self, board):
        actions = np.zeros(self.num_actions)

        for i in range(self.n_coin_action):
            actions[i] = 1

        for i in range(self.n_coin_action, self.num_actions):
            card_position = i - self.n_coin_action
            if self.is_possible_to_buy(board, card_position):
                actions[i] = 1

        return actions

    def get_coins(self, board, x):
        candidated_ids = get_coin_comb(x)
        for ids in candidated_ids:
            color = Element(ids).name
            if self.is_possible_to_get_coin(board, color):
                self.get_a_coin(board, color)
    
    def is_possible_to_get_coin(self, board, color):
        if board.coins[color] > 0:
            return True
        else:
            return False

    def get_a_coin(self, board, color):
        if board.coins[color] > 0:
            board.coins[color] -= 1
            self.coins[color] += 1
            print('{} get a {} coin.'.format(self.name, color))
        else:
            pass

    def is_possible_to_buy(self, board, card_position):
        card = board.flatten_table_cards[card_position]
        price = card.price
        price = adjust_price(price, self.sum_development_card_gem)

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
        assert(card_position>=0 and card_position<=self.n_buy_action)

        if self.is_possible_to_buy(board, card_position):
            card = board.flatten_table_cards[card_position]
            price = card.price
            price = adjust_price(price, self.sum_development_card_gem)
            
            for key in self.coins.keys():
                if key=="GOLD":
                    pass
                else:
                    self.coins[key] -= int(price[Element[key].value])
                    board.coins[key] += int(price[Element[key].value])

            self.development_cards.append(card)
            self._update_score()
            
            print('{} get a {} card.'.format(self.name, card))

            board.update_table_development_card(card)

            self.update_noble_cards(board)
            self._update_score()

        else:
            print('Not enough tokens.')

    def update_noble_cards(self, board):
        for card in board.noble_cards:
            if self.is_get_possible_noble_card(card):
                self.noble_cards.append(card)
                board.noble_cards.remove(card)
                print('Get {} card.'.format(card))

    def is_get_possible_noble_card(self, card):
        price = card.price
        gem_status = self.sum_development_card_gem
        is_possible = True
        for i in range(5):
            if gem_status[i] < price[i]:
                is_possible = False
                break

        return is_possible

    def print_status(self, object_name=None):
        if object_name is not None:
            print("[{}]".format(object_name))

        print("Development cards: ")
        l1_cards = []
        l2_cards = []
        l3_cards = []
        for card in self.development_cards:
            if card.level==1:
                l1_cards.append(card)
            if card.level==2:
                l2_cards.append(card)
            if card.level==3:
                l3_cards.append(card)

        print(l1_cards)
        print(l2_cards)
        print(l3_cards)
        
        print("Noble cards: ")
        print(self.noble_cards)
        print("Coin status: ")
        print(self.coins)    
        print("Victory point: {}".format(self.sum_victory_point))
        print("")

