from jsplendor.card.card_development import get_all_cards, get_level_cards

def main():
    # check level1 cards.
    l1_cards = get_level_cards(level=1)
    assert (len(l1_cards)==40), "Some level1 cards are missing."
    l1_price_sum = 0
    l1_victory_point_sum = 0
    for idx, card in enumerate(l1_cards):
        print(idx)
        card.print_info()
        assert(card.level == 1)
        l1_victory_point_sum += card.victory_point
        l1_price_sum += sum(card.price)

    assert(l1_victory_point_sum==5)
    assert(l1_price_sum==165)

    # check level2 cards.
    l2_cards = get_level_cards(level=2)
    assert (len(l2_cards)==30), "Some level2 cards are missing."
    l2_price_sum = 0
    l2_victory_point_sum = 0
    for idx, card in enumerate(l2_cards):
        print(idx)
        card.print_info()
        assert(card.level == 2)
        l2_victory_point_sum += card.victory_point
        l2_price_sum += sum(card.price)

    assert(l2_victory_point_sum==55)
    assert(l2_price_sum==205)

    # check level3 cards.
    l3_cards = get_level_cards(level=3)
    assert (len(l3_cards)==20), "Some level3 cards are missing."
    l3_price_sum = 0
    l3_victory_point_sum = 0
    for idx, card in enumerate(l3_cards):
        print(idx)
        card.print_info()
        assert(card.level == 3)
        l3_victory_point_sum += card.victory_point
        l3_price_sum += sum(card.price)

    assert(l3_victory_point_sum==80)
    assert(l3_price_sum==215)

    print('done')


if __name__ == "__main__":
    main()