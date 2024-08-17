from jsplendor.card import get_noble_cards

def test_noble_card():
    cards = get_noble_cards()

    price_white = 0
    price_blue = 0
    price_green = 0
    price_red = 0
    price_black = 0

    for card in cards:
        price_white += card.price[0]
        price_blue += card.price[1]
        price_green += card.price[2]
        price_red += card.price[3]
        price_black += card.price[4]

    assert(price_white==17)
    assert(price_blue==17)
    assert(price_green==17)
    assert(price_red==17)
    assert(price_black==17)

    print('done')
    

if __name__ == "__main__":
    main()