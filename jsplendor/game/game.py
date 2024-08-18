from jsplendor.game import Board
from jsplendor.game import Player
from jsplendor.card import get_all_development_cards, get_three_noble_cards
from jsplendor.coin import get_full_coin_for_board, get_empty_coin

class Game:
    def __init__(self):
        all_development_cards = get_all_development_cards()
        selected_noble_cards = get_three_noble_cards()
        board_coins = get_full_coin_for_board()
        self.board = Board(
                    name="board",
                    development_cards=all_development_cards,
                    noble_cards=selected_noble_cards,
                    coins=board_coins)
        
        player1_coins = get_empty_coin()
        self.player1 = Player(
                        name="player1",
                        development_cards=[],
                        noble_cards=[],
                        coins=player1_coins)
        
        self.component_list = [self.board, self.player1]

        print("Initial game status")
        self.print_status()

        self.step = 0
        self.check_all_coins()
        self.check_all_cards()

    def print_status(self):
        self.board.print_status(object_name="board")
        self.player1.print_status(object_name="player1")

    def step(self):
        pass

    def check_all_coins(self):
        sum_white = 0
        sum_blue = 0
        sum_green = 0
        sum_red = 0
        sum_black = 0
        sum_gold = 0

        for component in self.component_list:
            sum_white += component.coins["WHITE"]
            sum_blue += component.coins["BLUE"]
            sum_green += component.coins["GREEN"]
            sum_red += component.coins["RED"]
            sum_black += component.coins["BLACK"]
            sum_gold += component.coins["GOLD"]

        assert(sum_white==4)
        assert(sum_blue==4)
        assert(sum_green==4)
        assert(sum_red==4)
        assert(sum_black==4)
        assert(sum_gold==5)

    def check_all_cards(self):
        sum_developement_cards = 0
        sum_noble = 0

        for component in self.component_list:
            if isinstance(component, Board):
                sum_developement_cards += len(component.level1_cards) + len(component.table_level1)
                sum_developement_cards += len(component.level2_cards) + len(component.table_level2)
            else:  # player
                sum_developement_cards += len(component.development_cards)

            sum_noble += len(component.noble_cards)

        assert(sum_developement_cards == 40+30)  # level1 + level2
        assert(sum_noble == 3)
