from jsplendor.game import Board
from jsplendor.game import Player
from jsplendor.card import get_all_development_cards, get_three_noble_cards
from jsplendor.coin import get_full_coin_for_board, get_empty_coin


def test_game_component():
    all_development_cards = get_all_development_cards()
    selected_noble_cards = get_three_noble_cards()
    board_coins = get_full_coin_for_board()
    board = Board(development_cards=all_development_cards,
                  noble_cards=selected_noble_cards,
                  coins=board_coins)
    
    player1_coins = get_empty_coin()
    player1 = Player(development_cards=[],
                     noble_cards=[],
                     coins=player1_coins)
    
    player2_coins = get_empty_coin()
    player2 = Player(development_cards=[],
                     noble_cards=[],
                     coins=player2_coins)
    
    board.print_status(object_name="board")
    player1.print_status(object_name="player1")
    player2.print_status(object_name="player2")
    
    print('done')


if __name__ == "__main__":
    test_game_component()


