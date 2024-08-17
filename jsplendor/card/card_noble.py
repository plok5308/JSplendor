import random
# price array - [(w)hite, bl(u)e, (g)reen, (r)ed, blac(k)]
# price array - [w, u, g, r, k]

# VP / price 
noble_list = [
    (3, [0, 0, 4, 4, 0]),
    (3, [3, 0, 0, 3, 3]),
    (3, [4, 4, 0, 0, 0]),
    (3, [4, 0, 0, 0, 4]),
    (3, [0, 4, 4, 0, 0]),
    (3, [0, 3, 3, 3, 0]),
    (3, [3, 3, 3, 0, 0]),
    (3, [0, 0, 0, 4, 4]),
    (3, [3, 3, 0, 0, 3]),
    (3, [0, 0, 3, 3, 3]),
]

class NobleCard:
    def __init__(self, victory_point, price):
        self.victory_point = victory_point
        self.price = price

    def print(self):
        print("noble price: {}".format(self.price))

def get_noble_cards():
    noble_cards = []
    for data in noble_list:
        card = NobleCard(victory_point=data[0],
                  price=data[1])
        noble_cards.append(card)
        
    return noble_cards

def get_three_noble_cards():
    noble_cards = get_noble_cards()
    selected_noble_cards = random.sample(noble_cards, 3)
    return selected_noble_cards


