from jsplendor.game import Game

def test_game():
    game = Game()

    for i in range(10):
        print('='*30)
        print('step {}'.format(i))
        print('='*30)
        game.player1.get_a_coin(game.board, "WHITE")
        game.player1.get_a_coin(game.board, "BLUE")
        game.player1.get_a_coin(game.board, "BLACK")

        game.print_status()

    game.player1.buy_development_card(game.board, card_position=0)
    game.print_status()

    print('done')
    

if __name__ == "__main__":
    test_game()