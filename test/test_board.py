from jsplendor.game import Board
from jsplendor.card import get_all_development_cards, get_three_noble_cards
from jsplendor.coin import get_full_coin_for_board, get_empty_coin


def test_board():
    all_development_cards = get_all_development_cards()
    selected_noble_cards = get_three_noble_cards()
    board_coins = get_full_coin_for_board()
    board = Board(
                name="board",
                development_cards=all_development_cards,
                noble_cards=selected_noble_cards,
                coins=board_coins)
    
    res_sum = 0
    for i in range(40):
        res = board.lay_level_card_on_table(level=1)
        res_sum += res

    assert(res_sum==-1 * board.level1_n)

    res_sum = 0
    for i in range(30):
        res = board.lay_level_card_on_table(level=2)
        res_sum += res

    assert(res_sum==-1 * board.level1_n)
    print('done')
    

if __name__ == "__main__":
    test_board()